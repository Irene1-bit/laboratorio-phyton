# 
# File: es9.py
# Author: Irene De Luca 
# Date: 26cle/06/2026
# Version: 1.0
# Description: esercizio 9
#




import argparse  # Gestisce l'analisi degli argomenti passati da riga di comando (CLI)
import random  # Consente di estrarre caratteri casuali e mescolare liste
import string  # Fornisce gruppi di caratteri predefiniti (lettere, cifre, ecc.)
import json  # Permette di leggere, formattare e scrivere dati in formato JSON
import os  # Fornisce funzioni per interagire con il file system del sistema operativo
from datetime import datetime  # Permette di ottenere data e ora correnti per lo storico


# ECCEZIONI CUSTOM



class CriteriaError(Exception):  # Definisce un'eccezione personalizzata che eredita dalla classe base Exception
    """Sollevata quando i criteri richiesti per la password sono impossibili

    da soddisfare (es. lunghezza troppo corta per i caratteri richiesti).
    """

    pass  # Segnaposto necessario per completare la definizione di una classe vuota


# GENERAZIONE PASSWORD


def genera_password(
    lunghezza=12, maiuscole=True, numeri=True, simboli=True
):  # Definisce la funzione generatrice con parametri di default
    """Genera una password casuale rispettando i criteri richiesti.

    Garantisce che ci sia ALMENO un carattere per ogni categoria attiva,
    mescolando poi il tutto per non avere pattern prevedibili.
    """
    pool = list(
        string.ascii_lowercase
    )  # Inizializza il pool di caratteri partendo dalle lettere minuscole
    obbligatori = (
        []
    )  # Crea una lista vuota per raccogliere i caratteri minimi richiesti dalle opzioni

    if maiuscole:  # Se il parametro 'maiuscole' è impostato su True
        pool += list(
            string.ascii_uppercase
        )  # Aggiunge le lettere maiuscole al pool totale dei caratteri
        obbligatori.append(
            random.choice(string.ascii_uppercase)
        )  # Seleziona una maiuscola casuale e la mette negli obbligatori
    if numeri:  # Se il parametro 'numeri' è impostato su True
        pool += list(
            string.digits
        )  # Aggiunge i numeri da 0 a 9 sotto forma di caratteri al pool
        obbligatori.append(
            random.choice(string.digits)
        )  # Seleziona una cifra casuale e la inserisce negli obbligatori
    if simboli:  # Se il parametro 'simboli' è impostato su True
        simboli_ammessi = (
            "!@#$%&*?+-"  # Definisce la stringa contenente i caratteri speciali consentiti
        )
        pool += list(
            simboli_ammessi
        )  # Aggiunge i simboli speciali definiti al pool globale dei caratteri
        obbligatori.append(
            random.choice(simboli_ammessi)
        )  # Estrae un simbolo a caso e lo unisce alla lista degli obbligatori

    if lunghezza < len(
        obbligatori
    ):  # Verifica se la lunghezza richiesta è minore del numero di caratteri obbligatori
        raise CriteriaError(  # Solleva l'eccezione personalizzata per impedire la generazione
            f"Lunghezza {lunghezza} troppo corta per rispettare tutti i criteri richiesti "  # Specifica la lunghezza troppo corta richiesta
            f"(servono almeno {len(obbligatori)} caratteri)."  # Segnala la lunghezza minima calcolata come necessaria
        )  # Termina la chiamata dell'eccezione CriteriaError

    # riempiamo il resto della password a caso dal pool
    resto = [
        random.choice(pool) for _ in range(lunghezza - len(obbligatori))
    ]  # Genera una lista di caratteri casuali per completare la lunghezza richiesta

    caratteri = (
        obbligatori + resto
    )  # Unisce la lista dei caratteri di sicurezza obbligatori con quelli del resto
    random.shuffle(
        caratteri
    )  # Mescola gli elementi della lista sul posto per eliminare sequenze prevedibili
    return "".join(
        caratteri
    )  # Converte la lista di singoli caratteri in una stringa e la restituisce


# ANALISI DI ROBUSTEZZA (uso di lambda)


# Ogni criterio è una lambda: prende la password e restituisce True/False.
# Tenerli in un dizionario rende piu facile aggiungerne di nuovi.
CRITERI = {
    "lunghezza >= 8": lambda p: len(p)
    >= 8,  # Verifica se la lunghezza della password p è maggiore o uguale a 8 caratteri
    "lunghezza >= 12": lambda p: len(p)
    >= 12,  # Verifica se la lunghezza della password p è maggiore o uguale a 12 caratteri
    "contiene minuscole": lambda p: any(
        c.islower() for c in p
    ),  # Verifica se c'è almeno un carattere minuscolo all'interno della stringa p
    "contiene maiuscole": lambda p: any(
        c.isupper() for c in p
    ),  # Controlla se è presente almeno una lettera maiuscola nella stringa p
    "contiene numeri": lambda p: any(
        c.isdigit() for c in p
    ),  # Ritorna True se trova almeno una cifra numerica nella stringa p
    "contiene simboli": lambda p: any(
        c in "!@#$%&*?+-_." for c in p
    ),  # Cerca se uno o più simboli ammessi sono inclusi nella stringa p
    "nessuno spazio": lambda p: " "
    not in p,  # Verifica che non ci siano spazi bianchi all'interno della stringa p
}


def valuta_password(password):
    """Applica tutti i criteri e restituisce punteggio = numero di criteri

    soddisfatti su totale. dettagli = dizionario {nome_criterio: bool}
    """
    dettagli = {
        nome: funzione(password) for nome, funzione in CRITERI.items()
    }  # Crea un dizionario eseguendo ogni lambda del dizionario CRITERI sulla password
    punteggio = sum(
        dettagli.values()
    )  # Somma i valori booleani (True=1, False=0) per ottenere il punteggio totale
    return (
        punteggio,
        dettagli,
    )  # Restituisce una tupla contenente il punteggio numerico e il report dettagliato


def valutazione_testuale(punteggio, totale_criteri):
    """Converte il punteggio numerico in un giudizio leggibile."""
    percentuale = (
        punteggio / totale_criteri
    )  # Calcola il rapporto tra criteri superati e criteri totali
    if percentuale == 1.0:  # Se tutti i criteri sono stati superati al 100%
        return "Eccellente"  # Ritorna il giudizio massimo
    elif percentuale >= 0.7:  # Se è stato superato almeno il 70% dei controlli
        return "Forte"  # Ritorna un giudizio di sicurezza elevato
    elif (
        percentuale >= 0.4
    ):  # Se è stato soddisfatto tra il 40% e il 69% dei requisiti
        return "Media"  # Assegna una valutazione intermedia
    else:  # In tutti gli altri casi (sotto il 40% di conformità)
        return "Debole"  # Assegna una valutazione di vulnerabilità


# STORICO SU FILE (JSON)


FILE_STORICO = os.path.join(
    os.path.dirname(__file__), "storico.json"
)  # Ricava la cartella dello script corrente e definisce il percorso assoluto del file JSON


def maschera(password):
    """Non salviamo mai la password in chiaro: solo lunghezza e iniziale."""
    if not password:  # Se la stringa della password è vuota o None
        return ""  # Restituisce una stringa vuota di sicurezza
    return password[0] + "*" * (
        len(password) - 1
    )  # Prende la prima lettera e sostituisce i restanti caratteri con degli asterischi


def log_azione(azione, **dettagli):
    """Funzione di logging generica: 'azione' è obbligatorio, **dettagli

    raccoglie un numero variabile di informazioni aggiuntive (packing).
    """
    voce = {
        "data": datetime.now().isoformat(timespec="seconds"),
        "azione": azione,
    }  # Crea un dizionario iniziale con data/ora in formato ISO (precisione secondi) e tipo azione
    voce.update(
        dettagli
    )  # Unisce i parametri aggiuntivi dinamici passati alla funzione dentro il dizionario 'voce'

    storico = (
        []
    )  # Inizializza una lista vuota destinata a contenere tutti i log di gioco
    if os.path.exists(
        FILE_STORICO
    ):  # Controlla preventivamente se il file di storico JSON esiste già sul disco
        with open(
            FILE_STORICO, "r", encoding="utf-8"
        ) as f:  # Apre il file JSON in modalità lettura con codifica caratteri UTF-8
            try:  # Tenta di decodificare il contenuto del file
                storico = json.load(
                    f
                )  # Carica i vecchi log convertendoli da JSON a lista di dizionari Python
            except (
                json.JSONDecodeError
            ):  # Gestisce l'errore nel caso in cui il file JSON sia vuoto o corrotto
                storico = (
                    []
                )  # Reimposta lo storico come lista vuota per evitare blocchi o crash

    storico.append(
        voce
    )  # Aggiunge la nuova voce di log in coda alla lista dello storico

    with open(
        FILE_STORICO, "w", encoding="utf-8"
    ) as f:  # Apre lo stesso file in modalità scrittura per salvare le modifiche
        json.dump(
            storico, f, indent=2, ensure_ascii=False
        )  # Scrive lo storico formattato in modo leggibile (indentazione 2 spazi) sul file


def mostra_storico():
    """Stampa a schermo lo storico in formato leggibile."""
    if not os.path.exists(
        FILE_STORICO
    ):  # Se il file dello storico non è ancora presente sul disco
        print("Nessuno storico presente ancora.")  # Avvisa l'utente a schermo
        return  # Interrompe l'esecuzione del comando e torna al chiamante

    with open(
        FILE_STORICO, "r", encoding="utf-8"
    ) as f:  # Apre il file di log in modalità lettura
        storico = json.load(
            f
        )  # Converte l'intero archivio JSON in una lista Python

    if not storico:  # Se la lista caricata è vuota (es. file inizializzato ma senza dati)
        print("Storico vuoto.")  # Avvisa l'utente
        return  # Termina l'esecuzione del comando

    print(
        f"{'Data':<20} {'Azione':<10} {'Dettagli'}"
    )  # Stampa la riga di intestazione della tabella con spaziatura a sinistra fissa
    print("-" * 60)  # Stampa una linea divisoria fatta di trattini lunga 60 caratteri
    for voce in storico:  # Itera su ciascun elemento (dizionario di log) registrato nello storico
        data = voce.pop(
            "data"
        )  # Estrae la data eliminando contemporaneamente la chiave dal dizionario temporaneo
        azione = voce.pop(
            "azione"
        )  # Rimuove ed estrae il nome dell'azione per formattarla separatamente
        dettagli = ", ".join(
            f"{k}={v}" for k, v in voce.items()
        )  # Costruisce una stringa formattata unendo le coppie chiave=valore rimaste
        print(
            f"{data:<20} {azione:<10} {dettagli}"
        )  # Mostra a schermo la riga di log con le colonne perfettamente incolonnate


# CLI CON ARGPARSE


def comando_genera(args):  # Funzione richiamata dal parser quando viene scelto il sotto-comando 'genera'
    for _ in range(
        args.quantita
    ):  # Esegue un ciclo per quante volte indicato dal parametro '--quantita'
        try:  # Tenta di chiamare la funzione di generazione password
            pwd = genera_password(  # Salva la password generata in una variabile locale 'pwd'
                lunghezza=args.lunghezza,  # Passa il valore numerico dell'argomento '--lunghezza'
                maiuscole=not args.no_maiuscole,  # Passa l'opposto logico del flag '--no-maiuscole' (se attivo, esclude le maiuscole)
                numeri=not args.no_numeri,  # Passa il valore opposto di '--no-numeri'
                simboli=not args.no_simboli,  # Passa il valore opposto di '--no-simboli'
            )  # Chiude la chiamata a genera_password
        except (
            CriteriaError
        ) as e:  # Cattura l'errore se le opzioni di generazione sono incompatibili
            print(f"Errore: {e}")  # Mostra l'errore generato a schermo
            return  # Termina immediatamente l'esecuzione del comando

        punteggio, dettagli = valuta_password(
            pwd
        )  # Esegue l'analisi di robustezza sulla password appena creata
        giudizio = valutazione_testuale(
            punteggio, len(CRITERI)
        )  # Traduce il punteggio in un giudizio leggibile (es. "Forte")
        print(
            f"{pwd}   ->   {giudizio} ({punteggio}/{len(CRITERI)})"
        )  # Mostra la password generata in chiaro con il relativo livello di sicurezza

        log_azione(  # Scrive l'operazione nel file di storico JSON
            "genera",  # Definisce il nome dell'azione da registrare
            lunghezza=args.lunghezza,  # Registra la lunghezza impostata
            password=maschera(
                pwd
            ),  # Registra la versione protetta/mascherata della password
            punteggio=f"{punteggio}/{len(CRITERI)}",  # Memorizza il punteggio di robustezza ottenuto
            giudizio=giudizio,  # Memorizza il giudizio testuale associato
        )  # Chiude la chiamata a log_azione


def comando_verifica(args):  # Funzione richiamata dal parser quando viene usato il sotto-comando 'verifica'
    punteggio, dettagli = valuta_password(
        args.password
    )  # Valuta la robustezza della stringa passata come argomento dal terminale
    giudizio = valutazione_testuale(
        punteggio, len(CRITERI)
    )  # Converte il risultato in una valutazione verbale

    print(
        f"\nPassword: {maschera(args.password)}"
    )  # Mostra a schermo la password oscurata per privacy
    print(
        f"Giudizio: {giudizio}  ({punteggio}/{len(CRITERI)} criteri soddisfatti)\n"
    )  # Mostra il giudizio generale e la frazione di criteri superati
    for (
        nome,
        ok,
    ) in (
        dettagli.items()
    ):  # Scorre tutti i singoli dettagli dei criteri analizzati
        simbolo = (
            "OK" if ok else "X "
        )  # Definisce il marker grafico visivo: "OK" se superato, "X" se fallito
        print(
            f"  [{simbolo}] {nome}"
        )  # Stampa l'esito di conformità del singolo criterio a schermo

    log_azione(  # Scrive l'operazione di verifica nello storico
        "verifica",  # Definisce il tipo di operazione effettuata
        password=maschera(
            args.password
        ),  # Salva la password in forma mascherata per sicurezza
        punteggio=f"{punteggio}/{len(CRITERI)}",  # Registra il punteggio di robustezza calcolato
        giudizio=giudizio,  # Memorizza il verdetto finale del controllo
    )  # Chiude la chiamata di inserimento nel log


def comando_storico(
    args,
):  # Funzione invocata dal parser quando viene inserito il comando 'storico'
    mostra_storico()  # Chiama semplicemente la funzione che stampa a schermo i dati del JSON


def crea_parser():  # Definisce la struttura, i parametri e le opzioni accettati dalla riga di comando
    parser = argparse.ArgumentParser(  # Crea l'istanza principale del parser di argomenti CLI
        description="PasswordLab: genera e verifica la robustezza delle password."  # Descrizione dell'utility mostrata usando l'aiuto (-h)
    )
    sotto = parser.add_subparsers(
        dest="comando", required=True
    )  # Definisce un gruppo di sotto-comandi (genera, verifica, storico) obbligatori

    p_genera = sotto.add_parser(
        "genera", help="Genera una o più password"
    )  # Aggiunge il sotto-comando 'genera' al sistema CLI
    p_genera.add_argument(
        "--lunghezza", type=int, default=12
    )  # Aggiunge l'opzione opzionale '--lunghezza' di tipo intero (default 12)
    p_genera.add_argument(
        "--quantita", type=int, default=1
    )  # Aggiunge l'opzione opzionale '--quantita' per generare più password insieme
    p_genera.add_argument(
        "--no-maiuscole", action="store_true"
    )  # Specifica un flag booleano per escludere l'uso delle maiuscole
    p_genera.add_argument(
        "--no-numeri", action="store_true"
    )  # Definisce il flag booleano per escludere i caratteri numerici
    p_genera.add_argument(
        "--no-simboli", action="store_true"
    )  # Definisce il flag booleano per evitare i caratteri speciali
    p_genera.set_defaults(
        func=comando_genera
    )  # Collega direttamente questo sotto-comando alla funzione di esecuzione 'comando_genera'

    p_verifica = sotto.add_parser(
        "verifica", help="Verifica la robustezza di una password"
    )  # Aggiunge il sotto-comando 'verifica' al sistema CLI
    p_verifica.add_argument(
        "password", type=str
    )  # Richiede obbligatoriamente come argomento posizionale la stringa della password da testare
    p_verifica.set_defaults(
        func=comando_verifica
    )  # Associa questo sotto-comando alla funzione 'comando_verifica'

    p_storico = sotto.add_parser(
        "storico", help="Mostra lo storico delle operazioni"
    )  # Configura il sotto-comando 'storico' all'interno della CLI
    p_storico.set_defaults(
        func=comando_storico
    )  # Associa il sotto-comando alla funzione di lettura e visualizzazione 'comando_storico'

    return parser  # Restituisce l'oggetto parser configurato pronto all'uso


def main():  # Punto di ingresso dell'applicazione all'avvio dello script
    parser = (
        crea_parser()
    )  # Costruisce e configura il parser CLI richiamando la funzione dedicata
    args = (
        parser.parse_args()
    )  # Legge e analizza gli argomenti passati effettivamente dall'utente nel terminale
    args.func(
        args
    )  # Chiama dinamicamente la funzione registrata nei default (func) del sotto-comando selezionato


if (
    __name__ == "__main__"
):  # Verifica se lo script viene eseguito direttamente dall'utente (non importato come modulo)
    main()  # Esegue la funzione principale avviando il flusso di esecuzione del software