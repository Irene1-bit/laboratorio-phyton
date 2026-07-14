#
# File: es1.py
#
# Author: Irene De Luca 
#
# Date: 14/03/2026
#
# Version: 1.0
#
# Description: esercizio 1
#



def is_pari(n):
    """Restituisce True se n è pari, False se è dispari."""
    return n % 2 == 0


def genera_numero():
    """Chiede all'utente un numero intero positivo.
    Continua a chiedere finché l'input non è un intero valido e > 0."""
    while True:
        testo = input("Inserisci un numero intero positivo: ")

        try:
            numero = int(testo)
        except ValueError:
            print("Devi inserire un numero intero (es. 7, non 'sette' o 7.5).")
            continue

        if numero <= 0:
            print("Il numero deve essere positivo.")
            continue

        return numero


def genera_sequenza(numero):
    """Costruisce la sequenza di Collatz a partire da 'numero':
    - se pari, il prossimo termine è numero / 2
    - se dispari, il prossimo termine è numero * 3 + 1
    Si ferma quando arriva a 1 oppure supera 100 elementi."""
    sequenza = [numero]
    n = numero

    while n != 1 and len(sequenza) < 100:
        if is_pari(n):
            n = n // 2
        else:
            n = n * 3 + 1
        sequenza.append(n)

    return sequenza


def analizza_sequenza(lista):
    """Restituisce (massimo, lunghezza, somma) della sequenza data."""
    massimo = max(lista)
    lunghezza = len(lista)
    somma = sum(lista)
    return massimo, lunghezza, somma


def ricerca(lista):
    """Stampa i numeri della sequenza divisibili per 5.
    Se non ce ne sono, stampa un messaggio dedicato."""
    divisibili = [n for n in lista if n % 5 == 0]

    if divisibili:
        print(f"Numeri divisibili per 5 nella sequenza: {divisibili}")
    else:
        print("Nessun numero della sequenza è divisibile per 5.")


def chiedi_quanti_numeri():
    """Chiede quanti numeri l'utente vuole testare in totale (>= 1)."""
    while True:
        testo = input("Quanti numeri vuoi testare? ")

        try:
            quanti = int(testo)
        except ValueError:
            print("Devi inserire un numero intero.")
            continue

        if quanti <= 0:
            print("Il numero deve essere maggiore di zero.")
            continue

        return quanti


def main():
    quanti = chiedi_quanti_numeri()

    risultati = []  # lista di tuple (numero_iniziale, lunghezza_sequenza)

    for indice in range(quanti):
        print(f"\n--- Numero {indice + 1} di {quanti} ---")

        numero = genera_numero()
        sequenza = genera_sequenza(numero)
        massimo, lunghezza, somma = analizza_sequenza(sequenza)

        print(f"Sequenza generata: {sequenza}")
        print(f"Valore massimo raggiunto: {massimo}")
        print(f"Lunghezza della sequenza: {lunghezza}")
        print(f"Somma di tutti i numeri: {somma}")
        ricerca(sequenza)

        risultati.append((numero, lunghezza))

    # --- Riepilogo finale ---
    print("\n=== Riepilogo finale ===")
    for numero, lunghezza in risultati:
        print(f"  Numero iniziale {numero} -> sequenza di lunghezza {lunghezza}")

    numero_vincente, lunghezza_vincente = max(risultati, key=lambda coppia: coppia[1])
    print(f"\nIl numero che ha generato la sequenza più lunga è {numero_vincente} "
          f"(lunghezza {lunghezza_vincente}).")


if __name__ == "__main__":
    main()
