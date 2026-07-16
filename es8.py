# 
# File: es8.py
# Author: Irene De Luca 
# Date: 10/06/2026
# Version: 1.0
# Description: esercizio 8
#



# Importa il modulo 'json' per leggere il file contenente il dizionario delle parole
import json
# Importa il modulo 'os' per interagire con il sistema operativo (es. verificare l'esistenza di file)
import os
# Importa il modulo 'random' per poter estrarre casualmente una parola dalla lista
import random

# Definisce il nome del file JSON da cui caricare le parole di gioco
FILE_PAROLE = "parole.json"
# Definisce il numero massimo di errori consentiti prima di perdere la partita
TENTATIVI_MAX = 6


def carica_parole(percorso):
    """Legge la lista di parole da un file JSON, controllando OGNI
    precondizione PRIMA di procedere (stile LBYL)."""

    # 1) controllo che il file esista, prima di provare ad aprirlo
    # Usa os.path.exists per verificare se il percorso fornito è valido ed esistente sul disco
    if not os.path.exists(percorso):
        # Se il file non esiste, stampa un messaggio di errore informativo
        print(f"Errore: il file '{percorso}' non esiste.")
        # Restituisce None per indicare che il caricamento è fallito
        return None

    # Apre in sicurezza il file JSON in modalità lettura ('r') e con codifica dei caratteri UTF-8
    with open(percorso, "r", encoding="utf-8") as f:
        # Analizza e converte il contenuto del file JSON in una struttura dati Python (un dizionario)
        dati = json.load(f)

    # 2) controllo che la chiave 'parole' esista, prima di leggerla
    # Verifica esplicitamente che la stringa 'parole' sia presente tra le chiavi del dizionario appena caricato
    if "parole" not in dati:
        # Se manca la chiave richiesta, avvisa l'utente
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        # Restituisce None per bloccare la partita sul nascere
        return None

    # Estrae la lista delle parole associata alla chiave 'parole'
    lista_parole = dati["parole"]

    # 3) controllo che la lista non sia vuota, prima di scegliere a caso
    # Controlla la lunghezza della lista di parole per evitare che random.choice fallisca
    if len(lista_parole) == 0:
        # Se la lista è vuota, stampa un messaggio di errore
        print("Errore: la lista delle parole è vuota.")
        # Restituisce None impedendo l'avvio del gioco
        return None

    # Se tutti i controlli sono superati, seleziona una parola a caso dalla lista e la converte in minuscolo
    return random.choice(lista_parole).lower()


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Stampa lo stato corrente del gioco (parola mascherata, tentativi, lettere provate)."""
    # Costruisce la parola oscurata: mostra la lettera reale se è stata indovinata, altrimenti inserisce un trattino basso '_'
    # Unisce infine tutti i caratteri con uno spazio vuoto per facilitarne la lettura a schermo
    mascherata = " ".join(c if c in lettere_indovinate else "_" for c in parola)
    # Mostra all'utente la stringa della parola mascherata
    print(f"\nParola: {mascherata}")
    # Stampa il numero di tentativi rimanenti prima del game over
    print(f"Tentativi rimasti: {tentativi_rimasti}")
    # Stampa le lettere già provate in ordine alfabetico, mostrando '(nessuna)' se l'insieme è vuoto
    print(f"Lettere già tentate: {', '.join(sorted(lettere_tentate)) or '(nessuna)'}")


def gioca(parola):
    """Ciclo principale del gioco, in stile LBYL: ogni azione è preceduta
    da un controllo esplicito con if, mai da un try/except."""

    # Inizializza un insieme (set) vuoto per memorizzare le singole lettere indovinate dall'utente
    lettere_indovinate = set()
    # Inizializza un insieme (set) vuoto per tenere traccia di tutte le lettere inserite (giuste o sbagliate)
    lettere_tentate = set()
    # Imposta il conteggio dei tentativi rimasti al valore di TENTATIVI_MAX (6)
    tentativi_rimasti = TENTATIVI_MAX
    # Imposta lo stato della vittoria su False (non ancora vinto)
    vinto = False

    # Continua il ciclo finché ci sono tentativi disponibili e la partita non è ancora stata vinta
    while tentativi_rimasti > 0 and not vinto:
        # Chiama la funzione di supporto per visualizzare lo stato della sessione a ogni turno
        mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti)
        # Chiede l'input all'utente, rimuove spazi esterni (.strip()) e normalizza tutto in minuscolo (.lower())
        guess = input("Inserisci una lettera o prova l'intera parola: ").strip().lower()

        # Verifica se l'utente ha inserito un singolo carattere
        if len(guess) == 1:
            # --- guess di una singola lettera ---

            # controllo di validità PRIMA di usarla
            # Verifica se il carattere inserito è una lettera dell'alfabeto (esclude numeri, simboli o stringhe vuote)
            if not guess.isalpha():
                # Avvisa l'utente che il carattere non è idoneo
                print("Inserisci una lettera valida (a-z).")
                # Salta il resto del ciclo e ne richiede uno nuovo
                continue

            # controllo se già tentata PRIMA di riprovarla
            # Verifica se la lettera inserita è già presente nell'insieme dei tentativi effettuati
            if guess in lettere_tentate:
                # Avvisa l'utente del tentativo duplicato
                print(f"Hai già provato la lettera '{guess}'.")
                # Salta il resto del codice per richiedere un nuovo input
                continue

            # Aggiunge la lettera valida all'insieme di quelle tentate
            lettere_tentate.add(guess)

            # controllo se la lettera è nella parola PRIMA di decidere l'esito
            # Verifica se la lettera inserita fa effettivamente parte della parola segreta
            if guess in parola:
                # Aggiunge la lettera all'insieme di quelle indovinate
                lettere_indovinate.add(guess)
                # Notifica il successo della giocata
                print("Lettera corretta!")
            # Se la lettera non è presente nella parola
            else:
                # Sottrae un tentativo a quelli a disposizione del giocatore
                tentativi_rimasti -= 1
                # Notifica il fallimento della giocata
                print("Lettera sbagliata!")

        # Entra in questo blocco se l'utente ha provato a indovinare direttamente la parola intera
        else:
            # --- guess dell'intera parola ---
            # Controlla se la parola inserita coincide esattamente con la parola segreta
            if guess == parola:
                # Sblocca tutte le lettere inserendole nell'insieme delle lettere indovinate
                lettere_indovinate.update(parola)
                # Imposta lo stato di vittoria su True
                vinto = True
            # Se la parola inserita dall'utente è errata
            else:
                # Riduce di uno i tentativi disponibili
                tentativi_rimasti -= 1
                # Notifica l'errore commesso
                print("Parola sbagliata!")

        # controllo se tutte le lettere sono state indovinate
        # Verifica se l'insieme di lettere che compongono la parola è un sottoinsieme (<=) delle lettere indovinate
        if set(parola) <= lettere_indovinate:
            # Se tutte le lettere sono state scoperte, imposta il flag di vittoria su True
            vinto = True

    # Stampa una riga vuota per formattare l'output finale del terminale
    print()
    # Verifica se l'utente ha vinto la partita
    if vinto:
        # Stampa un messaggio di congratulazioni rivelando la parola segreta
        print(f"Hai indovinato! La parola era '{parola}'.")
    # Se i tentativi si sono esauriti e non si è indovinata la parola
    else:
        # Stampa il messaggio di sconfitta indicando la parola segreta corretta
        print(f"Hai esaurito i tentativi. La parola era '{parola}'.")


def main():
    # Avvia la funzione per caricare una parola segreta dal file JSON e la salva nella variabile 'parola'
    parola = carica_parole(FILE_PAROLE)

    # controllo che il caricamento sia andato a buon fine PRIMA di giocare
    # Verifica esplicitamente se la variabile 'parola' è vuota (None), sintomo di un errore nel caricamento del file
    if parola is None:
        # Mostra un messaggio di impossibilità ad avviare la sessione di gioco
        print("Impossibile avviare il gioco.")
        # Interrompe l'esecuzione del programma principale
        return

    # Avvia il ciclo di gioco vero e proprio passando la parola ottenuta
    gioca(parola)


# Assicura che la funzione main() venga eseguita solo quando lo script è lanciato direttamente e non importato altrove
if __name__ == "__main__":
    main()