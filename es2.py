#
# File: es2.py
#
# Author: Irene De Luca 
#
# Date: 25/03/2026
#
# Version: 1.0
#
# Description: esercizio 2
#



testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

# Caratteri di punteggiatura che vogliamo "staccare" dalle parole quando
# analizziamo il testo parola per parola.
PUNTEGGIATURA = ".,;:!?'\"()-"


def estrai_parole_pulite(blocco_testo):
    """Divide un blocco di testo in parole, togliendo la punteggiatura
    attaccata e riportando tutto in minuscolo, per confrontare le parole in modo uniforme."""
    parole_pulite = []
    for parola in blocco_testo.split():
        nucleo = parola.strip(PUNTEGGIATURA).lower()
        if nucleo:
            parole_pulite.append(nucleo)
    return parole_pulite


# 1. Contare le righe non vuote


def conta_righe_non_vuote(testo):
    righe = testo.split('\n')
    non_vuote = [riga for riga in righe if riga.strip() != '']
    return len(non_vuote)


# 2. Contare le parole

def conta_parole(testo):
    return len(testo.split())


# 3. Contare i caratteri alfanumerici


def conta_caratteri_alfanumerici(testo):
    return len([carattere for carattere in testo if carattere.isalnum()])


# 4. Contare quante volte compare una lettera data dall'utente


def conta_lettera(testo, lettera):
    lettera = lettera.lower()
    return len([carattere for carattere in testo.lower() if carattere == lettera])


# 5. Sostituire "day", "water", "about" con "PYTHON"


def sostituisci_parole(testo, parole_target, sostituto='PYTHON'):
    """Sostituisce ogni occorrenza (indipendentemente da maiuscole/minuscole)
    delle parole in 'parole_target' con 'sostituto', mantenendo la
    punteggiatura eventualmente attaccata (es. 'day,' -> 'PYTHON,')."""
    parole_target_lower = {p.lower() for p in parole_target}  # set comprehension

    righe_nuove = []
    for riga in testo.split('\n'):
        token_nuovi = []
        for token in riga.split(' '):
            nucleo = token.strip(PUNTEGGIATURA)
            if nucleo.lower() in parole_target_lower and nucleo != '':
                token_nuovi.append(token.replace(nucleo, sostituto))
            else:
                token_nuovi.append(token)
        righe_nuove.append(' '.join(token_nuovi))

    return '\n'.join(righe_nuove)


# 6. Parole in posizione dispari in maiuscolo (posizione contata per riga)

def maiuscolo_posizioni_dispari(testo):
    righe_nuove = []
    for riga in testo.split('\n'):
        parole_riga = riga.split()
        parole_nuove = []
        for indice, parola in enumerate(parole_riga, start=1):
            if indice % 2 == 1:
                parole_nuove.append(parola.upper())
            else:
                parole_nuove.append(parola)
        righe_nuove.append(' '.join(parole_nuove))
    return '\n'.join(righe_nuove)


# 7. Invertire l'ordine dei versi (dal basso all'alto)

def inverti_ordine_versi(testo):
    righe = testo.split('\n')
    return '\n'.join(righe[::-1])



# 8. Specchiare il secondo verso di ogni strofa

def specchia_secondo_verso_strofe(testo):
    strofe = testo.strip('\n').split('\n\n')  # le strofe sono separate da riga vuota
    strofe_nuove = []

    for strofa in strofe:
        righe = strofa.split('\n')
        if len(righe) >= 2:
            righe[1] = righe[1][::-1]  # slicing al contrario: specchia la stringa
        strofe_nuove.append('\n'.join(righe))

    return '\n\n'.join(strofe_nuove)



# 9. Parole comuni a TUTTE le strofe

def parole_comuni_a_tutte_le_strofe(testo):
    strofe = testo.strip('\n').split('\n\n')
    insiemi_parole = [set(estrai_parole_pulite(strofa)) for strofa in strofe]

    comuni = insiemi_parole[0]
    for insieme in insiemi_parole[1:]:
        comuni = comuni & insieme  # intersezione tra set

    return comuni


# 10. Lista univoca di tutte le parole, ordinata per lunghezza


def lista_univoca_parole_ordinata(testo):
    parole_pulite = estrai_parole_pulite(testo)
    parole_uniche = list(set(parole_pulite))  # il set toglie i duplicati
    parole_uniche.sort(key=len)
    return parole_uniche


# 11. Dizionario {carattere: occorrenze} per OGNI carattere del testo

def dizionario_occorrenze_caratteri(testo):
    occorrenze = {}
    for carattere in testo:
        if carattere in occorrenze:
            occorrenze[carattere] += 1
        else:
            occorrenze[carattere] = 1
    return occorrenze


# 12. Come sopra, ma solo caratteri alfanumerici, ignorando maiuscole/minuscole

def dizionario_occorrenze_alfanumerici(testo):
    occorrenze = {}
    for carattere in testo.lower():
        if carattere.isalnum():
            if carattere in occorrenze:
                occorrenze[carattere] += 1
            else:
                occorrenze[carattere] = 1
    return occorrenze


# MAIN: dimostra tutti i punti in ordine

def main():
    print("1. Righe non vuote:", conta_righe_non_vuote(testo))
    print("2. Numero di parole:", conta_parole(testo))
    print("3. Caratteri alfanumerici:", conta_caratteri_alfanumerici(testo))

    lettera = input("\n4. Inserisci una lettera da cercare nel testo: ")
    print(f"   La lettera '{lettera}' compare {conta_lettera(testo, lettera)} volte")

    print("\n5. Testo con 'day', 'water', 'about' sostituite da PYTHON:")
    print(sostituisci_parole(testo, ["day", "water", "about"]))

    print("\n6. Parole in posizione dispari in maiuscolo:")
    print(maiuscolo_posizioni_dispari(testo))

    print("\n7. Testo con i versi in ordine invertito:")
    print(inverti_ordine_versi(testo))

    print("\n8. Secondo verso di ogni strofa specchiato:")
    print(specchia_secondo_verso_strofe(testo))

    print("\n9. Parole comuni a tutte le strofe:")
    comuni = parole_comuni_a_tutte_le_strofe(testo)
    print(comuni if comuni else "(nessuna parola è comune a tutte le strofe)")

    print("\n10. Lista univoca delle parole, ordinata per lunghezza:")
    print(lista_univoca_parole_ordinata(testo))

    print("\n11. Occorrenze di OGNI carattere (dizionario):")
    print(dizionario_occorrenze_caratteri(testo))

    print("\n12. Occorrenze dei soli caratteri alfanumerici (case-insensitive):")
    print(dizionario_occorrenze_alfanumerici(testo))


if __name__ == "__main__":
    main()