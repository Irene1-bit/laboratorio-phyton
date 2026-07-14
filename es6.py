#
# File: es6.py
#
# Author: Irene De Luca 
#
# Date: 30/04/2026
#
# Version: 1.0
#
# Description: esercizio 6
#




from rubrica import Rubrica

AZIONI_VALIDE = {"APRI", "AGGIUNGI", "RIMUOVI", "SALVA", "STAMPA", "EXIT"}


def menu():
    print("\nAzioni disponibili: APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA, EXIT")


def main():
    rubrica = Rubrica()  # rubrica vuota e non ancora aperta

    print("=== Gestione Rubrica ===")
    menu()

    while True:
        azione = input("\nCosa vuoi fare? ").strip().upper()

        if azione not in AZIONI_VALIDE:
            print(f"Azione '{azione}' non riconosciuta.")
            menu()
            continue

        if azione == "EXIT":
            print("Uscita dal programma. Arrivederci!")
            break

        elif azione == "APRI":
            percorso = input("Percorso del file da aprire (JSON o testo): ").strip()
            rubrica.apri(percorso)

        elif azione == "AGGIUNGI":
            nome = input("Nome del contatto: ").strip()
            telefono = input("Telefono: ").strip()
            email = input("Email: ").strip()
            rubrica.aggiungi(nome, telefono, email)

        elif azione == "RIMUOVI":
            nome = input("Nome del contatto da rimuovere: ").strip()
            rubrica.rimuovi(nome)

        elif azione == "STAMPA":
            nome = input("Nome del contatto da stampare: ").strip()
            rubrica.stampa(nome)

        elif azione == "SALVA":
            percorso = input("Percorso del file su cui salvare (JSON o testo): ").strip()
            rubrica.salva(percorso)


if __name__ == "__main__":
    main()