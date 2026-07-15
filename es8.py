import json
import os
import random

FILE_PAROLE = "parole.json"
TENTATIVI_MAX = 6


def carica_parole(percorso):
    """Legge la lista di parole da un file JSON, controllando OGNI
    precondizione PRIMA di procedere (stile LBYL)."""

    # 1) controllo che il file esista, prima di provare ad aprirlo
    if not os.path.exists(percorso):
        print(f"Errore: il file '{percorso}' non esiste.")
        return None

    with open(percorso, "r", encoding="utf-8") as f:
        dati = json.load(f)

    # 2) controllo che la chiave 'parole' esista, prima di leggerla
    if "parole" not in dati:
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None

    lista_parole = dati["parole"]

    # 3) controllo che la lista non sia vuota, prima di scegliere a caso
    if len(lista_parole) == 0:
        print("Errore: la lista delle parole è vuota.")
        return None

    return random.choice(lista_parole).lower()


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Stampa lo stato corrente del gioco (parola mascherata, tentativi, lettere provate)."""
    mascherata = " ".join(c if c in lettere_indovinate else "_" for c in parola)
    print(f"\nParola: {mascherata}")
    print(f"Tentativi rimasti: {tentativi_rimasti}")
    print(f"Lettere già tentate: {', '.join(sorted(lettere_tentate)) or '(nessuna)'}")


def gioca(parola):
    """Ciclo principale del gioco, in stile LBYL: ogni azione è preceduta
    da un controllo esplicito con if, mai da un try/except."""

    lettere_indovinate = set()
    lettere_tentate = set()
    tentativi_rimasti = TENTATIVI_MAX
    vinto = False

    while tentativi_rimasti > 0 and not vinto:
        mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti)
        guess = input("Inserisci una lettera o prova l'intera parola: ").strip().lower()

        if len(guess) == 1:
            # --- guess di una singola lettera ---

            # controllo di validità PRIMA di usarla
            if not guess.isalpha():
                print("Inserisci una lettera valida (a-z).")
                continue

            # controllo se già tentata PRIMA di riprovarla
            if guess in lettere_tentate:
                print(f"Hai già provato la lettera '{guess}'.")
                continue

            lettere_tentate.add(guess)

            # controllo se la lettera è nella parola PRIMA di decidere l'esito
            if guess in parola:
                lettere_indovinate.add(guess)
                print("Lettera corretta!")
            else:
                tentativi_rimasti -= 1
                print("Lettera sbagliata!")

        else:
            # --- guess dell'intera parola ---
            if guess == parola:
                lettere_indovinate.update(parola)
                vinto = True
            else:
                tentativi_rimasti -= 1
                print("Parola sbagliata!")

        # controllo se tutte le lettere sono state indovinate
        if set(parola) <= lettere_indovinate:
            vinto = True

    print()
    if vinto:
        print(f"Hai indovinato! La parola era '{parola}'.")
    else:
        print(f"Hai esaurito i tentativi. La parola era '{parola}'.")


def main():
    parola = carica_parole(FILE_PAROLE)

    # controllo che il caricamento sia andato a buon fine PRIMA di giocare
    if parola is None:
        print("Impossibile avviare il gioco.")
        return

    gioca(parola)


if __name__ == "__main__":
    main()