#
# File: es5.py
#
# Author: Irene De Luca 
#
# Date: 22/04/2026
#
# Version: 1.0
#
# Description: esercizio 5
#





import random
import time

def stessa_diagonale(x0, y0, x1, y1):   
    # Calcola la distanza tra le colonne (x1 - x0) e la distanza tra le righe (y1 - y0).
    # Se i valori assoluti (abs) sono uguali, significa che le regine sono sulla stessa diagonale.

    return abs(x1 - x0) == abs(y1 - y0) 


def incrocia_colonne(posizioni, col):    
    # Confronta la regina della colonna attuale ('col') con tutte quelle posizionate prima.
    # Il ciclo scorre tutte le colonne precedenti (da 0 fino a col - 1).
    for c in range(col):
        # Se la regina precedente alla colonna 'c' incrocia in diagonale la regina alla colonna 'col'
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True # C'è un conflitto
    return False # Nessun conflitto trovato con le colonne precedenti


def soluzione_ok(soluzione): 
    # Verifica se l'intera scacchiera è valida.
    # Scorre le colonne partendo dalla seconda (indice 1) fino all'ultima (indice 7).
    for col in range(1, len(soluzione)): 
        # Se la regina in questa colonna si scontra con una di quelle a sinistra
        if incrocia_colonne(soluzione, col):
            return False # La configurazione non è valida, scartala
    return True # Se arriva alla fine senza conflitti, la scacchiera è perfetta


#rotazione sulla scacchiera
def ruota_90(sol):
    N = len(sol)       # N è la dimensione della scacchiera (8)
    nuova = [0]*N      # Crea una nuova lista vuota di 8 elementi per metterci la scacchiera ruotata
    
    # Scorre ogni riga 'r' della scacchiera originale
    for r in range(N):
        c = sol[r]             # Trova in quale colonna 'c' si trova la regina alla riga 'r'
        nuova[c] = N - 1 - r   # Applica la formula geometrica per spostare la regina dopo la rotazione di 90°
    return nuova


def ruota_180(sol):
    # Ruotare di 180° equivale a prendere la scacchiera e ruotarla di 90° per due volte di fila
    return ruota_90(ruota_90(sol))


def ruota_270(sol):
    # Ruotare di 270° equivale a fare prima una rotazione di 180° e poi un'altra da 90°
    return ruota_90(ruota_180(sol))

def main(): 
    N = 8 # La scacchiera è 8x8
    random_generator = random.Random() # Inizializza il generatore di numeri casuali
    base = list(range(N)) # Crea la lista di partenza: [0, 1, 2, 3, 4, 5, 6, 7]

    soluzioni_uniche = [] # Questa lista conterrà le 10 soluzioni diverse che troveremo
    ripetizioni = {}      # Un dizionario per contare quante volte indoviniamo la stessa soluzione
    tempi = []            # Lista in cui salveremo il tempo impiegato per trovare ciascuna soluzione
    tentativi_totali = 0  # Contatore globale di quanti mescolamenti a caso facciamo in totale

    # Il ciclo esterno continua finché non abbiamo collezionato 10 soluzioni uniche
    while len(soluzioni_uniche) < 10: 
        tentativi = 0            # Azzera i tentativi per la ricerca della singola soluzione corrente
        start = time.time()      # Registra l'orario di partenza di questa ricerca

        # Questo ciclo interno continua a provare finché non "indovina" una soluzione valida
        while True:
            tentativi += 1          # Incrementa i tentativi di questo round
            tentativi_totali += 1   # Incrementa i tentativi totali generali

            candidato = base[:] # Crea una copia della lista base [0, 1, 2... 7]
            random_generator.shuffle(candidato) # Mescola la copia a caso (es. [3, 0, 4, 7, 1, 6, 2, 5])

            # Controlla se la combinazione mescolata a caso non ha regine che si attaccano
            if soluzione_ok(candidato): 
                chiave = tuple(candidato) # Converte la lista in tupla (perché i dizionari richiedono chiavi immutabili)

                # Gestione del conteggio delle ripetizioni nel dizionario
                if chiave in ripetizioni:
                    ripetizioni[chiave] += 1 # Se l'avevamo già trovata in passato, aumenta il contatore di 1
                else:
                    ripetizioni[chiave] = 1  # Se è la prima volta che esce, imposta il contatore a 1

                # Se questa soluzione valida non l'avevamo mai salvata prima
                if candidato not in soluzioni_uniche:
                    tempo = time.time() - start # Calcola quanti secondi sono passati dallo 'start'

                    soluzioni_uniche.append(candidato) # Salva la nuova soluzione nella lista
                    tempi.append(tempo)                # Salva il tempo impiegato

                    # Stampa a schermo i dettagli della soluzione appena scoperta
                    print(f"Soluzione {len(soluzioni_uniche)}: {candidato}")
                    print(f" Tentativi: {tentativi}")
                    print(f" Tempo: {tempo:.4f}s\n")

                    break # Interrompe il ciclo 'while True' interno e passa alla prossima soluzione

    # --- STATISTICHE FINALI ---
    # Una volta trovate tutte e 10 le soluzioni, il programma esce dal ciclo principale e stampa i dati aggregati
    
    # Calcola il tempo medio facendo la somma di tutti i tempi diviso 10
    print("Tempo medio:", sum(tempi)/len(tempi))
    print("Tentativi totali:", tentativi_totali)

    print("\nRipetizioni:")
    # Scorre il dizionario delle ripetizioni
    for k in ripetizioni:
        # Se una soluzione è stata generata casualmente più di una volta, la stampa
        if ripetizioni[k] > 1:
            print(k, "ripetuta", ripetizioni[k], "volte")

    print("\nSimmetrie:")
    # Prende solo le prime 5 soluzioni uniche trovate e per ognuna mostra le sue rotazioni nello spazio
    for sol in soluzioni_uniche[:5]:
        print("\nBase:", sol)
        print("90° :", ruota_90(sol))
        print("180°:", ruota_180(sol))
        print("270°:", ruota_270(sol))