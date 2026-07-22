#
# File: es3.py
#
# Author: Irene De Luca 
#
# Date: 04/04/2026
#
# Version: 1.0
#
# Description: esercizio 3
#

import argparse


"rubrica base"
rubrica = {
'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
'Ron Weasley': {'giorno': 1, 
                'mese': 'marzo', 
                'anno': 1980, 
                'età': 46, 
                'sesso': 'M', 
                'mail': 'ron_weasley80@hogwards.uk'},
'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

#creo il parser per leggere i comandi dal terminale
parser = argparse.ArgumentParser()
parser.add_argument('--stampa', action='store_true') #serve per dire che azione frae, se nello script scrivo --stampa si attiverà quella, la parte dopo serve per non inserire un testo o un valore dopo
parser.add_argument('--eta', action='store_true')
parser.add_argument('--inversa', action='store_true')
parser.add_argument('--messaggi', action='store_true')
parser.add_argument('--nome')
parser.add_argument('--chiave')

args = parser.parse_args()

#punto1
'''stampa tutta la rubrica'''
if args.stampa: #in abse a che comando scrivo userà una di queste
    for nome in rubrica:
        print(nome, rubrica[nome])

#punto2
'''ordinale persone per età'''
if args.eta:
    ordinata = sorted(rubrica.items(), key=lambda x: x[1]['età'])   #Dice a sorted() di ordinare gli elementi guardando
                                                                    #dentro x[1] (il dizionario con i dati) la chiave 'età'.
    for nome, dati in ordinata:
        print(nome, dati['età'])

#punto3
'''ordina per età ma al contrario'''
if args.inversa:
    ordinata = sorted(rubrica.items(), key=lambda x: x[1]['età'], reverse=True) #inerte dal piu grande al piu piccolo
    for nome, dati in ordinata:
        print(nome, dati['età'])

#punto4
'''stampa un messaggio per ogni persona'''
if args.messaggi:
    for nome, dati in rubrica.items():
        saluto = "o" if dati['sesso'] == "M" 
else "a"
        print(f"Car{saluto} {nome},")
        print(f"sei nat{saluto} il {dati['giorno']} di {dati['mese']} del {dati['anno']} e hai {dati['età']} anni.")  
        print(f"Mail:{dati['mail']}")

#punto5
'''cerca una persona specifica per nome'''
if args.nome:
    if args.nome in rubrica:
        dati = rubrica[args.nome]
        saluto = "o" if dati['sesso'] == "M" else "a"
        print(f"""
    Car{saluto} {args.nome},
    sei nat{saluto} il {dati['giorno']} di {dati['mese']} del {dati['anno']} e hai {dati['età']} anni.  Ti manderemo gli auguri a {dati['mail']}""")
    else:
        print("Nome non trovato")

#punot6
'''cerca una chiave in tutte le persone'''
if args.chiave:
    for nome in rubrica:
        if args.chiave in rubrica[nome]:
            print(nome, rubrica[nome][args.chiave])


