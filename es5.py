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

def risolvi_punti_5_e_6():
    generatore = random.Random()   ##Creiamo l'oggetto generatore del modulo random che ci servirà per generare una soluzione possibile 
    
    N = 8   #Partiamo dalla classsica scacchiera 8x8 e poi la facciamo crescere
    while True:      #Facciamo partire un while infinito che si fermerà solo con il comando break
        scacchiera = list(range(N))     #Creiamo una lista di N elementi vuota 
        start_time = time.time()    #Facciamo partire il cronometro che ci servirà per il punto 6
        soluzione_trovata = False    #Definiamo una bandiera che ci servirà successivamente 
        
        print(f"Cerco 1 soluzione per scacchiera {N}x{N}...")
        
        # Continua a cercare finché non passano 15 secondi 
        while (time.time() - start_time) < 15:
            generatore.shuffle(scacchiera)   #Mescola casualmente la lista NxN
            if soluzione_ok(scacchiera):   #Se la permutazione della scacchiera va bene 
                soluzione_trovata = True   #abbiamo trovato una soluzione valida in un certo tempo che viene calcolato dopo
                tempo_impiegato = time.time() - start_time
                print(f"   Soluzione trovata in {tempo_impiegato} secondi!")
                break   #Se abbiamo trovato una soluzione in meno di 15 secondi allora possiamo concludere questo while perchè non ci interessa trovarne un'altra per questa dimensione 
                
        if soluzione_trovata:     #Se per la scacchiera NxN abbiamo trovato una soluzione in meno di 15 secondi (la bandiera è alzata, a valore true) passiamo alla dimensione superiore 
            N += 1 # Passa alla scacchiera più grande
        else:   #Se invece soluzione_trovata = false allora vuol dire che per questo N non abbiamo trovato una soluzione in meno di 15 secondi 
            #Se non l'abbiamo trovato allora lo diciamo a video e diciamo a video qual è la dimensione massima su cui
            #siamo riusciti a trovare una soluzione in meno di 15 secondi, ovvero quella prima di N 
            print(f"   Nessuna soluzione trovata in meno di 15s per N={N}.")
            print(f"-> Il lato N più grande risolvibile in < 15s è N={N-1}.")
            break   #finiamo il while esternop perchè abbiamo risolto il punto 6 trovando la dimensione massima 


#Passiamo alla soluzione dell'ultimo punto, ovvero il punto 7: 
#Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi. 
#Scrivete delle funzioni che, una volta trovata una soluzione alla scacchiera, costruiscano le 4 
#soluzioni simmetriche per rotazione. Trovate 5 soluzioni “uniche” e le rispettive soluzioni 
#simmetriche per rotazione per una scacchiera 8x8

#Definiamo prima di tutto una funzione che presa la scacchiera la ruota di 90 gradi. In input questa
#funzione prende la combinazione da ruotare di 90 gradi e la dimensione della scacchiera 
def ruota_90_gradi(posizioni, N):
    nuova_pos = [0] * N      #Creiamo una lista con tutti 0 di dimensione N dove andremo a posizionare le regine una volta ruotata la scacchiera 
    for r in range(N):      #A questo punto scorriamo la lista che indica le vecchie posizioni delle regine e calcoliamo le nuove (chiaramente non serve scorrere tutta la scacchiera, 64 posizioni, perchè considerando la lista eliminiamo tutti gli 0 e consideriamo solo le posizioni delle regine)
        c = posizioni[r]    #Così facendo so che la regina si troverà in coordinate (r, posizioni[r]) ovvero (r, c)
        #Come trovare la nuova posizione della regina una volta ruotata la scacchiera di 90 gradi (rotazione di una matrice di 90 gradi): 
        #Nuova riga = vecchia colonna 
        #Nuova colonna = si ottiene partendo dall'estremità destra della scacchiera (N - 1) e sottraendovi la vecchia coordinata "riga"
        nuovo_r = c
        nuovo_c = N - 1 - r
        nuova_pos[nuovo_r] = nuovo_c    #Riempiamo la nuova lista con le nuovew posizioni delle regine a seguito della rotazione 
    return tuple(nuova_pos)    #Ritorniamo la lista come tupla perchè in seguito dovremo verificarne l'unicità e questa cosa non si può fare con le liste in quanto modificabili



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
    print(f"soluzioni punti 5 e 6:") 
    risolvi_punti_5_e_6()

    print("\nSimmetrie:")
    # Prende solo le prime 5 soluzioni uniche trovate e per ognuna mostra le sue rotazioni nello spazio
    for sol in soluzioni_uniche[:5]:
        print("\nBase:", sol)
        print("90° :", ruota_90(sol))
        print("180°:", ruota_180(sol))
        print("270°:", ruota_270(sol))

main()