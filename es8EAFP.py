# 
# File: es8.py
# Author: Irene De Luca 
# Date: 10/06/2026
# Version: 1.0
# Description: esercizio 8
#




# Importa il modulo 'json' per decodificare il file di dati
import json

# Importa il modulo 'random' per scegliere la parola segreta
import random

# Nome del file JSON contenente le parole
FILE_PAROLE = "parole.json"
# Numero massimo di errori concessi al giocatore
TENTATIVI_MAX = 6


def carica_parola(percorso):
    """Carica una parola segreta in puro stile EAFP (proviamo l'azione, se fallisce gestiamo l'eccezione)."""

    # --- EAFP 1: Lettura del file ---
    # Proviamo ad aprire e leggere direttamente il file senza prima verificare se esiste
    try:
        with open(percorso, "r", encoding="utf-8") as f:
            dati = json.load(f)
    # Se il file non esiste sul disco, viene sollevata FileNotFoundError
    except FileNotFoundError:
        print(f"Errore: il file '{percorso}' non esiste.")
        return None
    # Se il file contiene testo malformato, viene sollevata JSONDecodeError
    except json.JSONDecodeError:
        print(f"Errore: il file '{percorso}' non è un JSON valido.")
        return None

    # --- EAFP 2: Estrazione della chiave 'parole' e della parola casuale ---
    # Proviamo ad accedere direttamente alla chiave e ad estrarre l'elemento
    try:
        lista_parole = dati["parole"]
        return random.choice(lista_parole).lower()
    # Se la chiave 'parole' manca nel dizionario, Python solleva KeyError
    except KeyError:
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None
    # Se la lista 'parole' è vuota, random.choice solleva IndexError
    except IndexError:
        print("Errore: la lista delle parole è vuota.")
        return None


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Visualizza lo stato corrente della partita."""

    # Costruisce la parola oscurata: mostra la lettera reale se indovinata, altrimenti '_'
    mascherata = " ".join(c if c in lettere_indovinate else "_" for c in parola)

    # Stampa le informazioni di gioco
    print(f"\nParola: {mascherata}")
    print(f"Tentativi rimasti: {tentativi_rimasti}")

    # EAFP: Proviamo a stampare l'insieme convertito in lista ordinata
    print(
        f"Lettere già tentate: {', '.join(sorted(lettere_tentate)) or '(nessuna)'}"
    )


def gioca(parola):
    """Ciclo principale del gioco scritto in stile EAFP chiaro e piatto."""

    # Insieme per tenere traccia delle lettere indovinate
    lettere_indovinate = set()
    # Usiamo un dizionario invece di un set per mostrare l'uso di KeyError in EAFP
    lettere_tentate = {}
    # Contatore dei tentativi rimasti
    tentativi_rimasti = TENTATIVI_MAX

    # Ciclo di gioco principale
    while tentativi_rimasti > 0:

        # Controllo della condizione di vittoria (tutte le lettere della parola sono state scoperte)
        if set(parola) <= lettere_indovinate:
            print(f"\nHai indovinato! La parola era '{parola}'.")
            return

        # Mostra la situazione attuale
        mostra_stato(
            parola, lettere_indovinate, lettere_tentate, tentativi_rimasti
        )

        # Acquisisce l'input pulendolo da spazi e rendendolo minuscolo
        guess = (
            input("Inserisci una lettera o prova l'intera parola: ")
            .strip()
            .lower()
        )

        # Ignora l'input se l'utente si limita a premere Invio
        if not guess:
            continue

        # --- CASO 1: L'utente inserisce una singola lettera ---
        if len(guess) == 1:

            # --- EAFP: Controllo se la lettera è già stata tentata ---
            # Proviamo a leggere la chiave nel dizionario delle lettere tentate
            try:
                # Se l'accesso ha successo, significa che la lettera è già stata usata
                valore = lettere_tentate[guess]
                print(f"Hai già provato la lettera '{guess}'.")
                continue
            # Se la chiave non esiste, viene sollevata un'eccezione KeyError
            except KeyError:
                # Registriamo la lettera nel dizionario per i prossimi turni
                lettere_tentate[guess] = True

            # --- EAFP: Controllo presenza della lettera nella parola ---
            # Verifichiamo se la lettera appartiene alla parola segreta
            if guess in parola:
                lettere_indovinate.add(guess)
                print("Lettera corretta!")
            else:
                tentativi_rimasti -= 1
                print("Lettera sbagliata!")

        # --- CASO 2: L'utente tenta l'intera parola ---
        else:
            if guess == parola:
                print(
                    f"\nFantastico! Hai indovinato l'intera parola: '{parola}'."
                )
                return
            else:
                tentativi_rimasti -= 1
                print("Parola sbagliata!")

    # Se esce dal ciclo while, il giocatore ha esaurito i tentativi
    print(f"\nHai esaurito i tentativi. La parola era '{parola}'.")


def main():
    # Carica la parola usando la logica EAFP
    parola = carica_parola(FILE_PAROLE)

    # Verifica di sicurezza prima di avviare il gioco
    if parola is not None:
        gioca(parola)
    else:
        print("Impossibile avviare il gioco a causa di un errore nel file.")


# Avvio dello script principale
if __name__ == "__main__":
    main()