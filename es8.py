# 
# File: es8.py
# Author: Irene De Luca 
# Date: 10/06/2026
# Version: 1.0
# Description: esercizio 8
#



# Importa il modulo 'json' per leggere il file contenente la lista delle parole
import json

# Importa il modulo 'os' per effettuare controlli sul filesystem (es. verificare l'esistenza del file)
import os

# Importa il modulo 'random' per selezionare casualmente la parola segreta
import random

# Nome del file JSON contenente i dati di gioco
FILE_PAROLE = "parole.json"
# Numero massimo di tentativi falliti concessi al giocatore
TENTATIVI_MAX = 6


def carica_parola(percorso):
    """Carica la parola segreta"""

    # --- LBYL CONTROLLO 1: Esistenza del file ---
    # Verifica preventiva: il file esiste sul disco prima di provare ad aprirlo?
    if not os.path.exists(percorso):
        print(f"Errore: il file '{percorso}' non esiste.")
        return None

    # Apre il file JSON in lettura 
    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    # --- LBYL CONTROLLO 2: Presenza della chiave ---
    # Verifica preventiva: la chiave 'parole' esiste nel dizionario prima di accedervi?
    if "parole" not in dati:
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None

    # Estrae la lista associata alla chiave 'parole'
    lista_parole = dati["parole"]

    # --- LBYL CONTROLLO 3: Lista non vuota ---
    # Verifica preventiva: la lista contiene almeno un elemento prima di estrarre a sorte?
    if len(lista_parole) == 0:
        print("Errore: la lista delle parole è vuota.")
        return None

    # Se tutti i controlli LBYL sono superati, sceglie una parola a caso e la rende minuscola
    return random.choice(lista_parole).lower()


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Visualizza a schermo lo stato attuale della partita."""

    # Costruisce la parola mascherata: mostra la lettera se indovinata, altrimenti '_'
    mascherata = " ".join(c if c in lettere_indovinate else "_" for c in parola)

    # Stampa la parola parzialmente oscurata
    print(f"\nParola: {mascherata}")
    # Stampa i tentativi ancora a disposizione
    print(f"Tentativi rimasti: {tentativi_rimasti}")
    # Stampa l'elenco delle lettere provate ordinate alfabeticamente
    print(
        f"Lettere già tentate: {', '.join(sorted(lettere_tentate)) or '(nessuna)'}"
    )


def gioca(parola):
    """Gestisce il ciclo di gioco applicando rigorosamente controlli LBYL."""

    # set per memorizzare le lettere lette correttamente
    lettere_indovinate = set()
    # set per memorizzare tutti i caratteri o tentativi già inseriti
    lettere_tentate = set()
    # Contatore dei tentativi rimasti
    tentativi_rimasti = TENTATIVI_MAX

    # Esegue il ciclo finché il giocatore ha ancora tentativi a disposizione
    while tentativi_rimasti > 0:

        # LBYL CONTROLLO: Condizione di vittoria 
        # Verifica se tutte le lettere della parola sono incluse nell'insieme di quelle indovinate
        if set(parola) <= lettere_indovinate:
            print(f"\nHai indovinato! La parola era '{parola}'.")
            # Interrompe direttamente la funzione gioca() in caso di vittoria
            return

        # Mostra a schermo l'interfaccia aggiornata
        mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti)

        # Chiede l'input all'utente, rimuove spazi extra agli estremi e converte in minuscolo
        guess = (input("Inserisci una lettera o prova l'intera parola: ").strip().lower())

        # LBYL CONTROLLO: Input vuoto 
        # Verifica preventiva: l'utente ha premuto Invio senza scrivere nulla?
        if len(guess) == 0:
            print("Non hai inserito alcun carattere!")
            continue

        # --- CASO 1: L'utente ha inserito una singola lettera ---
        if len(guess) == 1:

            # --- LBYL CONTROLLO: Carattere alfabetico ---
            # Verifica preventiva: l'input è una lettera dell'alfabeto (esclude cifre o simboli)?
            if not guess.isalpha():
                print("Inserisci una lettera valida (a-z).")
                continue

            # --- LBYL CONTROLLO: Tentativo duplicato ---
            # Verifica preventiva: la lettera è già presente nell'insieme dei tentativi effettuati?
            if guess in lettere_tentate:
                print(f"Hai già provato la lettera '{guess}'.")
                continue

            # Aggiunge la nuova lettera all'insieme di quelle tentate
            lettere_tentate.add(guess)

            # --- LBYL CONTROLLO: Esito della lettera ---
            # Verifica preventiva: la lettera inserita fa parte della parola segreta?
            if guess in parola:
                # Se presente, la aggiunge all'insieme di quelle indovinate
                lettere_indovinate.add(guess)
                print("Lettera corretta!")
            else:
                # Se assente, riduce di 1 i tentativi disponibili
                tentativi_rimasti -= 1
                print("Lettera sbagliata!")

        # --- CASO 2: L'utente prova a indovinare l'intera parola ---
        else:

            # --- LBYL CONTROLLO: Corrispondenza della parola ---
            # Verifica preventiva: la stringa inserita equivale esattamente alla parola segreta?
            if guess == parola:
                print(f"\nFantastico! Hai indovinato l'intera parola: '{parola}'.")
                # Esce subito dalla funzione 
                return
            else:
                # Se la parola è errata, scala un tentativo
                tentativi_rimasti -= 1
                print("Parola sbagliata!")

    # Se il ciclo while termina senza return, i tentativi si sono azzerati
    print(f"\nHai esaurito i tentativi. La parola era '{parola}'.")


def main():
    # Carica la parola segreta dal file JSON
    parola = carica_parola(FILE_PAROLE)

    # --- LBYL CONTROLLO: Esito del caricamento ---
    # Verifica preventiva: la variabile 'parola' contiene un valore valido prima di avviare il gioco?
    if parola is not None:
        gioca(parola)
    else:
        print("Impossibile avviare il gioco a causa di errori nel file.")


# Punto di ingresso principale del programma
if __name__ == "__main__":
    main()