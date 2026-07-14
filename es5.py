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

def stessa_diagonale(x0, y0, x1, y1):   #controlla se le due regine sono sulla stessa diagonale
    return abs(x1 - x0) == abs(y1 - y0) # se la distanza in x= distanza in y allora sono sulla stessa diagonale




def incrocia_colonne(posizioni, col):    #controllo se la regina nella colonna col entra in conflitto con quelle di prima
    for c in range(col):
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True
    return False

def soluzione_ok(soluzione): #controllo se la configurazione è valida
    for col in range(1, len(soluzione)): #controllo tutte le colonne
        if incrocia_colonne(soluzione, col):
            return False
    return True



#rotazione sulla scacchiera
def ruota_90(sol):
    N = len(sol)
    nuova = [0]*N
    for r in range(N):
        c = sol[r]
        nuova[c] = N - 1 - r   #nuova posizione trovata
    return nuova

def ruota_180(sol):
    return ruota_90(ruota_90(sol))

def ruota_270(sol):
    return ruota_90(ruota_180(sol))


def main(): #funzione principale
    N = 8 #dimensione scacchiera
    random_generator = random.Random()
    base = list(range(N)) #rapp una permutazione

    soluzioni_uniche = [] #soluzione senz duplicati
    ripetizioni = {} #conta quante volte esce una soluzione
    tempi = [] #tempi per ogni soluzione
    tentativi_totali = 0 #totale tentativi

    while len(soluzioni_uniche) < 10: #voglio 10 soluzioni diverse
        tentativi = 0
        start = time.time()

        while True:
            tentativi += 1
            tentativi_totali += 1

            candidato = base[:] #permutazione casuale
            random_generator.shuffle(candidato)

            if soluzione_ok(candidato): #controllo se è valida
                chiave = tuple(candidato)

                # conteggio ripetizioni
                if chiave in ripetizioni:
                    ripetizioni[chiave] += 1
                else:
                    ripetizioni[chiave] = 1

                # aggiungo solo se nuova
                if candidato not in soluzioni_uniche:
                    tempo = time.time() - start

                    soluzioni_uniche.append(candidato)
                    tempi.append(tempo)

                    print(f"Soluzione {len(soluzioni_uniche)}: {candidato}")
                    print(f" Tentativi: {tentativi}")
                    print(f" Tempo: {tempo:.4f}s\n")

                    break

    #statistica finale
    print("Tempo medio:", sum(tempi)/len(tempi))
    print("Tentativi totali:", tentativi_totali)
#stmapo solo quelle ripetute
    print("\nRipetizioni:")
    for k in ripetizioni:
        if ripetizioni[k] > 1:
            print(k, "ripetuta", ripetizioni[k], "volte")

    # simmetrie (ultime 5 soluzioni)
    print("\nSimmetrie:")
    for sol in soluzioni_uniche[:5]:
        print("\nBase:", sol)
        print("90° :", ruota_90(sol))
        print("180°:", ruota_180(sol))
        print("270°:", ruota_270(sol))


main()