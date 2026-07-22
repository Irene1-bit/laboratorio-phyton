#
# File: es1.py
#
# Author: Irene De Luca 
#
# Date: 14/03/2026
#
# Version: 1.0
#
# Description: chiede all'utente uno o piu numeri interi positivi e, per ciascuno, genera una sequenza seguendo la regola
#Si ripete finché il numero non arriva a 1 (o finché la sequenza non supera i 100 elementi, come sicurezza). Alla fine, per ogni sequenza, il programma calcola 
#alcune statistiche e mostra quali numeri della sequenza sono divisibili per 5.



def is_pari(n):     #dice se un numero è pari o dispari
    """Restituisce True se n è pari, False se è dispari."""
    return n % 2 == 0


def genera_numero(): #chiede il numero finchè non rispetta le condizioni
    """Chiede all'utente un numero intero positivo.
    Continua a chiedere finché l'input non è un intero valido e > 0."""
    while True:         #inizio un ciclo che fnisce solo se la conizione è falsa
        testo = input("Inserisci un numero intero positivo: ") #salva la risposta 

        try:        #se ho inserito un numero che rispetta le condizioni allora verrà convertito in int
            numero = int(testo)
        except ValueError:  #senno gestisce l'errore e stampa le stringa
            print("Devi inserire un numero intero ")
            continue       #Salta il resto del ciclo e torna subito all'inizio del while True, chiedendo nuovamente l'input.

        if numero <= 0: #qui controlla l'ultima condizione
            print("Il numero deve essere positivo.")
            continue

        return numero


def genera_sequenza(numero):
    """Costruisce la sequenza a partire da 'numero':
    - se pari, il prossimo termine è numero / 2
    - se dispari, il prossimo termine è numero * 3 + 1
    Si ferma quando arriva a 1 oppure supera 100 elementi."""
    sequenza = [numero]     #crea una lista con i numeri che inserisco
    n = numero

    while n != 1 and len(sequenza) < 100:
        if is_pari(n):
            n = n // 2
        else:
            n = n * 3 + 1
        sequenza.append(n) #aggiunge in coda n 

    return sequenza #resistuisce la lista completa


def analizza_sequenza(lista):
    """Restituisce (massimo, lunghezza, somma) della sequenza data."""
    massimo = max(lista)
    lunghezza = len(lista)
    somma = sum(lista)
    lista_sequenza=(massimo, lunghezza, somma)  #assegna la variabile lista_sequenza alla tupla
    return lista_sequenza


def ricerca(lista):
    """Stampa i numeri della sequenza divisibili per 5.
    Se non ce ne sono, stampa un messaggio dedicato."""
    divisibili = [n for n in lista if n % 5 == 0]   #list comprehension, crea un ciclo for piccolo in una riga
                                                    #il % calcola il resto
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


def main():         #Il main() non contiene la logica di calcolo: si limita 
                    #a chiamare le funzioni nel giusto ordine e a gestire il loop per ripetere l'operazione più volte. 
                    #Questo è il senso della lezione: dividere 
                    #un problema complesso in blocchi più piccoli, ognuno con la propria responsabilità.
    quanti = chiedi_quanti_numeri()

    risultati = []  # lista di tuple, prepara questa lista per salvare i dati di ogni numero 

    for indice in range(quanti):
        print(f"\n--- Numero {indice + 1} di {quanti} ---")     #intestazione per far sapere a che numero simao, c'è il +1 perche parteda zero

        numero = genera_numero()
        sequenza = genera_sequenza(numero)
        massimo, lunghezza, somma = analizza_sequenza(sequenza)

        print(f"Sequenza generata: {sequenza}")
        print(f"Valore massimo raggiunto: {massimo}")
        print(f"Lunghezza della sequenza: {lunghezza}")
        print(f"Somma di tutti i numeri: {somma}")
        ricerca(sequenza)

        risultati.append((numero, lunghezza))


    numero_vincente, lunghezza_vincente = max(risultati, key=lambda coppia: coppia[1])  #cerca il numero massimo, confronta non i numeri di partenza ma le lunghezza, quindi nella tupla non guara solo i primi numeri ma ancher la la lunghezza
    print(f"\nIl numero che ha generato la sequenza più lunga è {numero_vincente} "
          f"(lunghezza {lunghezza_vincente}).")


if __name__ == "__main__":
    main()  
