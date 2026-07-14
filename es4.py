#
# File: es4.py
#
# Author: Irene De Luca 
#
# Date: 14/04/2026
#
# Version: 1.0
#
# Description: esercizio 4
#



import argparse         #serve per leggere gli argomenti dal terminale
import json             #serve per lavorare con file JSON

rubrica = {
    'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
    'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

#creo il parser per leggere i comandi dal terminale
parser = argparse.ArgumentParser()
parser.add_argument('--file_testo', action='store_true')
parser.add_argument('--salva_json', action='store_true')
parser.add_argument('--leggi_json', action='store_true')

args = parser.parse_args()

#punto1
'''Scrivere rubrica su un file testo'''
if args.file_testo:
    file = open('rubrica.txt', 'w')       #crea file in scrittura

    for nome, dati in rubrica.items():    #scorre tutti i contatti
        riga = f"{nome}, {dati['giorno']}, {dati['mese']}, {dati['anno']}, {dati['età']}, {dati['sesso']}, {dati['mail']}\n"
        file.write(riga)  #crea una riga testo con i dati e la scrive nel file 

    file.close()        #chiude il file

#punto2
'''Salvarela rubrica in formato JSON'''
if args.salva_json:
    file = open('rubrica.json', 'w')        #apre file JSON in scrittura
    json.dump(rubrica, file)        #converte il dizionario in JSON
    file.close()        #chiude il file

#punto3
'''Legge il file JSON'''
if args.leggi_json:
    file = open('rubrica.json', 'r')        #apre file JSON in lettura
    dati = json.load(file)      #trasforma JSON in dizionario python
    file.close()        #chiude il file

    print(dati)     #stampa i dati letti


#COME USARE IL TERMINALE
#1-python3 es4.py --file_testo
#2-python es4.py --salva_json
#3-python es4.py --leggi_json