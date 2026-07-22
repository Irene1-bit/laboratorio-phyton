# 
# File: es7.py
# Author: Irene De Luca 
# Date: 25/05/2026
# Version: 1.0
# Description: esercizio 7
#

# Importa il modulo integrato 'time' per gestire le funzioni legate al tempo (usato per il cronometro)
import time


# PUNTO 1: GENERATORE DELLA TABELLINA


# Definisce una funzione generatrice che calcola i valori della tabellina
def genera_tabellina(numero, fino_a=10):
    """Generatore: produce i valori 0*numero, 1*numero, ..., fino_a*numero
    uno alla volta , invece di costruire subito tutta la lista."""
    # Avvia un ciclo che va da 0 fino al valore di "fino_a" (incluso, grazie a + 1)
    for moltiplicatore in range(fino_a + 1):
        # yield restituisce il risultato corrente e "mette in pausa" la funzione,
        # conservando lo stato per la chiamata successiva senza occupare memoria per l'intera lista
        yield moltiplicatore * numero


# DECORATORE: CRONOMETRA LA PARTITA

# Definisce un decoratore, ovvero una funzione che accetta un'altra funzione come parametro per estenderne il comportamento
def cronometra(funzione):
    """Decoratore: misura il tempo di esecuzione della funzione decorata,
    inoltrando tutti gli argomenti con l'unpacking *args/**kwargs
    (stesso schema visto a lezione per decorare funzioni con parametri)."""
    # Definisce la funzione interna (wrapper) che sostituirà temporaneamente la funzione originale.
    # Accetta qualsiasi tipo e numero di parametri posizionali (*args) e nominali (**kwargs)
    def wrapper(*args, **kwargs):
        # Registra il timestamp di inizio (in secondi dall'epoca Unix) prima di avviare la funzione
        inizio = time.time()
        # Esegue la funzione originale inoltrandole intatti tutti i parametri ricevuti
        risultato = funzione(*args, **kwargs)
        # Calcola la differenza tra il tempo attuale e quello di inizio per trovare i secondi trascorsi
        tempo_impiegato = time.time() - inizio
        # Stampa a schermo il tempo impiegato formattandolo con una sola cifra decimale (:.1f)
        print(f"\n(Tempo di gioco: {tempo_impiegato:.1f} secondi)")
        # Restituisce il valore originariamente prodotto dalla funzione decorata
        return risultato
    # Restituisce l'oggetto funzione wrapper appena definito, completando la struttura del decoratore
    return wrapper


# LAMBDA: VALUTAZIONE DEL PUNTEGGIO

# Definisce una funzione anonima (lambda) estremamente compatta per valutare la prestazione del giocatore.
# Prende in input il punteggio ottenuto e il totale delle domande e usa degli operatori ternari nidificati (if/else in linea).
valuta_punteggio = lambda punteggio, totale: (
    # Se il punteggio è uguale al totale, restituisce questo messaggio di successo assoluto
    "Perfetto, tabellina impeccabile!" if punteggio == totale else
    # Altrimenti, se il punteggio copre almeno il 70% (0.7) delle risposte corrette, restituisce un messaggio di incoraggiamento forte
    "Molto bene, quasi perfetto!" if punteggio >= totale * 0.7 else
    # In tutti gli altri casi (punteggio inferiore al 70%), restituisce questo messaggio
    "Continua ad esercitarti!"
)


# PUNTO 2, 3, 4, 5: IL LOOP DI GIOCO

# Definisce un insieme (set) di stringhe che l'utente può digitare per interrompere volontariamente il gioco
COMANDI_USCITA = {"esci", "exit", "quit"}


# Applica il decoratore "cronometra" alla funzione "gioca_tabellina" per misurare quanto dura la partita
@cronometra
def gioca_tabellina(numero, fino_a=10):
    """Ciclo principale del gioco: chiede all'utente il valore corrente
    della tabellina, uno alla volta, usando il generatore genera_tabellina.
    Gestisce input non validi (lettere, decimali, simboli) senza interrompersi,
    e un comando di uscita personalizzato."""

    # Inizializza il generatore creato in precedenza per la tabellina del numero scelto
    generatore = genera_tabellina(numero, fino_a)
    # Imposta a 0 il contatore delle risposte corrette date dall'utente
    punteggio = 0
    # Calcola il numero totale di domande previste per questa sessione (es. da 0 a 10 sono 11 domande)
    totale_domande = fino_a + 1

    # Avvia un ciclo for sul generatore. "enumerate" ci restituisce sia l'indice (il moltiplicatore, da 0 in poi)
    # sia il valore effettivo generato (il valore atteso della moltiplicazione)
    for moltiplicatore, valore_atteso in enumerate(generatore):
        # Mostra la domanda corrente all'utente nel terminale
        print(f"\nQuanto fa {moltiplicatore} x {numero}?")

        # Avvia un ciclo infinito di inserimento per gestire eventuali risposte errate o input non validi
        while True:
            # Chiede l'input all'utente e usa .strip() per rimuovere spazi bianchi accidentali all'inizio o alla fine
            risposta = input("La tua risposta (o 'esci' per uscire): ").strip()

            # PUNTO 5: Controlla se la risposta inserita (convertita in minuscolo) rientra tra i comandi di uscita
            if risposta.lower() in COMANDI_USCITA:
                # Stampa un messaggio di interruzione e mostra il punteggio parziale accumulato fino a quel momento
                print(f"\nHai chiuso il gioco. Punteggio: {punteggio}/{totale_domande}")
                # Interrompe l'intera funzione restituendo il punteggio parziale
                return punteggio

            # PUNTI 3+4: Gestione dei controlli di validità dell'input inserito dall'utente
            try:
                # Tenta di convertire la stringa inserita dall'utente in un numero intero (int)
                valore_utente = int(risposta)
            # Se la conversione fallisce 
            except ValueError:
                # Mostra un messaggio esplicativo di errore senza far crashare il programma
                print("Risposta non valida: inserisci un numero intero ")
                # Forza il ciclo "while True" a ricominciare da capo, saltando il resto del codice e richiedendo l'input
                continue

            # Se l'input è valido ed equivale esattamente al risultato matematico corretto
            if valore_utente == valore_atteso:
                # Conferma la risposta corretta all'utente
                print("Corretto!")
                # Incrementa il punteggio di 1 unità
                punteggio += 1
                # Interrompe il ciclo "while True" interno per passare alla domanda successiva del ciclo "for" principale
                break
            # Se il numero inserito è valido ma il risultato matematico è sbagliato
            else:
                # Avvisa dell'errore e suggerisce quale operazione l'utente deve riprovare a calcolare
                print(f"Sbagliato, riprova!")

    # Finito il ciclo for (tutte le domande completate), stampa il riepilogo finale del punteggio ottenuto
    print(f"\nHai completato la tabellina del {numero}! Punteggio: {punteggio}/{totale_domande}")
    # Chiama la funzione lambda "valuta_punteggio" per mostrare il commento personalizzato in base al risultato
    print(valuta_punteggio(punteggio, totale_domande))
    # Restituisce il punteggio finale (che verrà intercettato e stampato anche dal wrapper del decoratore cronometro)
    return punteggio


# INPUT INIZIALE E AVVIO DEL PROGRAMMA

# Definisce una funzione di supporto per l'acquisizione sicura del numero della tabellina da giocare
def chiedi_numero_tabellina():
    """Chiede all'utente quale tabellina vuole giocare, gestendo
    anche qui input non validi senza interrompere il programma."""
    # Ciclo infinito per garantire che l'utente non proceda finché non inserisce un valore corretto
    while True:
        # Chiede l'input all'utente rimuovendo gli spazi superflui
        risposta = input("Che tabellina vuoi giocare? (numero intero): ").strip()
        try:
            # Prova a convertire la scelta in un intero e a restituirla immediatamente interrompendo la funzione
            return int(risposta)
        # Se l'utente scrive qualcosa che non è un numero intero valido
        except ValueError:
            # Stampa un messaggio d'errore e ricomincia il ciclo richiedendo il valore
            print("Devi inserire un numero intero valido.")


# Definisce la funzione principale che funge da punto d'ingresso del programma
def main():
    # Stampa l'intestazione iniziale del gioco nel terminale
    print("=== Gioco delle tabelline ===")
    # Ottiene in modo sicuro il numero della tabellina scelta dall'utente tramite la funzione dedicata
    numero = chiedi_numero_tabellina()
    # Avvia la partita vera e propria passando il numero inserito
    gioca_tabellina(numero)

if __name__ == "__main__":
    main()