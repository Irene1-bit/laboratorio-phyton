#
# File: es5.py
#
# Author: Irene De Luca 
#
# Date: 20/04/2026
#
# Version: 1.0
#
# Description: esercizio 5
#




import argparse
import random
import time


# Funzioni di base (dalla dispensa) - già generiche rispetto a N

def stessa_diagonale(x0, y0, x1, y1):
    """Ritorna Vero se le posizioni (x0, y0) e (x1, y1) sono sulla stessa diagonale."""
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy


def incrocia_colonne(posizioni, col):
    """Ritorna Vero se la regina in posizione (col, posizioni[col]) incrocia
    la diagonale di qualcuna delle regine precedenti."""
    for c in range(col):
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True
    return False


def soluzione_ok(soluzione_posizioni):
    """Controlla se tutte le posizioni della permutazione sono valide
    (nessuna coppia di regine sulla stessa diagonale)."""
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False
    return True


def genera_permutazione_casuale(n, generatore):
    """Genera una permutazione casuale di [0, 1, ..., n-1]."""
    scacchiera = list(range(n))
    generatore.shuffle(scacchiera)
    return scacchiera


# Punti 1+2: trovare N soluzioni (anche ripetute), con tentativi e tempo


def trova_soluzione(n, generatore):
    """Cerca UNA soluzione valida per permutazioni casuali.
    Ritorna (soluzione, numero_tentativi, tempo_impiegato)."""
    tentativi = 0
    inizio = time.time()

    while True:
        tentativi += 1
        scacchiera = genera_permutazione_casuale(n, generatore)
        if soluzione_ok(scacchiera):
            tempo = time.time() - inizio
            return scacchiera, tentativi, tempo


def dieci_soluzioni(n, generatore, quante=10):
    """Punto 1+2: trova 'quante' soluzioni (n regine), stampando per
    ognuna i tentativi necessari e il tempo, poi la media di entrambi."""
    risultati = []
    for i in range(quante):
        soluzione, tentativi, tempo = trova_soluzione(n, generatore)
        risultati.append((soluzione, tentativi, tempo))
        print(f"Soluzione {i + 1}: {soluzione}  (tentativi: {tentativi}, tempo: {tempo:.4f}s)")

    tempo_medio = sum(r[2] for r in risultati) / len(risultati)
    tentativi_medi = sum(r[1] for r in risultati) / len(risultati)
    print(f"\nTempo medio per soluzione: {tempo_medio:.4f}s")
    print(f"Tentativi medi per soluzione: {tentativi_medi:.1f}")
    return risultati


# Punti 3+4: soluzioni UNICHE, contando le ripetizioni di ciascuna

def trova_soluzioni_uniche(n, quante_uniche, generatore):
    """Cerca soluzioni finché non se ne trovano 'quante_uniche' diverse
    tra loro. Tiene un conteggio di quante volte ciascuna soluzione unica
    viene ritrovata durante la ricerca (le soluzioni ripetute non
    vengono scartate: contribuiscono al conteggio ma non fanno crescere
    l'insieme delle soluzioni uniche)."""
    conteggio = {}  # tupla (immutabile, quindi usabile come chiave) -> numero di volte trovata
    tentativi_totali = 0
    inizio = time.time()

    while len(conteggio) < quante_uniche:
        tentativi_totali += 1
        scacchiera = genera_permutazione_casuale(n, generatore)
        if soluzione_ok(scacchiera):
            chiave = tuple(scacchiera)
            conteggio[chiave] = conteggio.get(chiave, 0) + 1

    tempo = time.time() - inizio
    print(f"Trovate {quante_uniche} soluzioni uniche in {tentativi_totali} tentativi totali ({tempo:.4f}s)\n")
    for soluzione, volte in conteggio.items():
        ripetuta = "" if volte == 1 else f"  <- trovata {volte} volte"
        print(f"  {list(soluzione)}{ripetuta}")

    return conteggio


# Punto 6: dimensione massima N risolvibile entro un tempo limite

def trova_dimensione_massima(generatore, tempo_limite=15.0, n_iniziale=8):
    """Aumenta N di uno in uno finché il tempo per trovare UNA soluzione
    non supera 'tempo_limite' secondi. Ritorna l'ultimo N risolto in tempo."""
    n = n_iniziale
    ultimo_n_ok = None

    while True:
        inizio = time.time()
        tentativi = 0
        trovato = False

        while time.time() - inizio < tempo_limite:
            tentativi += 1
            scacchiera = genera_permutazione_casuale(n, generatore)
            if soluzione_ok(scacchiera):
                trovato = True
                break

        tempo = time.time() - inizio

        if trovato:
            print(f"N={n}: soluzione trovata in {tempo:.2f}s ({tentativi} tentativi)")
            ultimo_n_ok = n
            n += 1
        else:
            print(f"N={n}: nessuna soluzione trovata entro {tempo_limite}s. Mi fermo.")
            break

    print(f"\nLa dimensione massima risolta entro {tempo_limite}s è N={ultimo_n_ok}")
    return ultimo_n_ok


# Punto 7: soluzioni simmetriche per rotazione (90, 180, 270 gradi)

def ruota_90(soluzione):
    """Ruota di 90 gradi (in senso orario) una soluzione rappresentata
    come lista [colonna_riga_0, colonna_riga_1, ...].
    Il punto (riga, colonna) diventa (colonna, N-1-riga)."""
    n = len(soluzione)
    nuova = [0] * n
    for riga, colonna in enumerate(soluzione):
        nuova[colonna] = n - 1 - riga
    return nuova


def soluzioni_simmetriche(soluzione):
    """Costruisce le 4 soluzioni ottenute ruotando quella data di
    0, 90, 180 e 270 gradi, componendo ripetutamente ruota_90."""
    rot_90 = ruota_90(soluzione)
    rot_180 = ruota_90(rot_90)
    rot_270 = ruota_90(rot_180)
    return {
        "0°": list(soluzione),
        "90°": rot_90,
        "180°": rot_180,
        "270°": rot_270,
    }


def mostra_rotazioni(n, quante_uniche, generatore):
    """Punto 7: trova 'quante_uniche' soluzioni uniche e per ognuna
    mostra le sue 4 rotazioni."""
    conteggio = trova_soluzioni_uniche(n, quante_uniche, generatore)

    print("\n--- Soluzioni simmetriche per rotazione ---")
    for soluzione in conteggio:
        rotazioni = soluzioni_simmetriche(list(soluzione))
        print(f"\nSoluzione base: {rotazioni['0°']}")
        for angolo in ("90°", "180°", "270°"):
            print(f"  rotazione {angolo}: {rotazioni[angolo]}")


# CLI con argparse

def crea_parser():
    parser = argparse.ArgumentParser(
        prog="esercizio5.py",
        description="Problema delle N regine con permutazioni casuali (Lezione 7 - Esercizio 5)"
    )

    parser.add_argument('--n', type=int, default=8,
                         help="Dimensione della scacchiera NxN (default: 8)")
    parser.add_argument('--dieci_soluzioni', action='store_true',
                         help="Punti 1+2: trova 10 soluzioni, mostra tempo e tentativi medi")
    parser.add_argument('--uniche', type=int, metavar='QUANTE',
                         help="Punti 3+4: trova QUANTE soluzioni uniche, contando le ripetizioni")
    parser.add_argument('--rotazioni', type=int, metavar='QUANTE',
                         help="Punto 7: trova QUANTE soluzioni uniche e mostra le loro rotazioni")
    parser.add_argument('--dimensione_massima', action='store_true',
                         help="Punto 6: cerca il lato N più grande risolvibile entro --tempo_limite")
    parser.add_argument('--tempo_limite', type=float, default=15.0,
                         help="Tempo limite in secondi per --dimensione_massima (default: 15)")

    return parser


def main():
    parser = crea_parser()
    args = parser.parse_args()

    generatore = random.Random()

    nessuna_opzione = not any([
        args.dieci_soluzioni, args.uniche, args.rotazioni, args.dimensione_massima
    ])
    if nessuna_opzione:
        parser.print_help()
        return

    if args.dieci_soluzioni:
        dieci_soluzioni(args.n, generatore)

    if args.uniche:
        trova_soluzioni_uniche(args.n, args.uniche, generatore)

    if args.rotazioni:
        mostra_rotazioni(args.n, args.rotazioni, generatore)

    if args.dimensione_massima:
        trova_dimensione_massima(generatore, tempo_limite=args.tempo_limite, n_iniziale=args.n)


if __name__ == "__main__":
    main()

