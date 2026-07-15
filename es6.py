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


import json

# ==========================================
# 1. DEFINIZIONE DELLA CLASSE RUBRICA
# ==========================================
class Rubrica:
    """Una classe per gestire una rubrica telefonica con i dati dei contatti"""

    def __init__(self, dizionario_iniziale=None):
        """Inizializza la rubrica con un dizionario"""
        self.contatti = dizionario_iniziale

    @classmethod
    def apri_da_json(cls, nome_file):
        """Inizializza la rubrica leggendo da un file JSON"""
        with open(nome_file, 'r') as f:
            dati = json.load(f)
        return cls(dati)

    @classmethod
    def apri_da_txt(cls, nome_file):
        """Inizializza la rubrica leggendo da un file di testo"""
        with open(nome_file, 'r') as f:
            contenuto = f.read()
            dati = eval(contenuto)
        return cls(dati)

    def aggiungi(self, nome, dati_contatto):
        """Aggiunge un elemento alla rubrica"""
        if self.contatti is None:
            print("Prima apri una rubrica")
            return
        self.contatti[nome] = dati_contatto

    def rimuovi(self, nome):
        """Rimuove un elemento dalla rubrica dato il nome"""
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota.")
            return
        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return
        del self.contatti[nome]

    def stampa(self, nome):
        """Stampa tutte le informazioni di un contatto dato il nome"""
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota.")
            return
        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return
        
        contatto = self.contatti[nome]
        print(f"Nome: {nome}")
        print(f"Nato il: {contatto['giorno']} {contatto['mese']} {contatto['anno']}")
        print(f"Età: {contatto['età']}")
        print(f"Sesso: {contatto['sesso']}")
        print(f"Mail: {contatto['mail']}")

    def salva(self, nome_file):
        """Salva la rubrica su file JSON o TXT"""
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota")
            return

        if nome_file.endswith(".json"):
            with open(nome_file, 'w') as f:
                json.dump(self.contatti, f, indent=4)
        else:
            with open(nome_file, 'w') as f:
                f.write(str(self.contatti))


# ==========================================
# 2. PROGRAMMA INTERATTIVO PRINCIPALE
# ==========================================
dati_rubrica = {
  'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
  'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
  'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
  'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

# Inizializziamo l'oggetto senza una rubrica aperta (None)
rubrica = Rubrica(None)

while True:
    azione = input("\nInserisci l'azione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA) o 'EXIT': ").strip().upper()

    if azione == "EXIT":
        print("Programma terminato.")
        break

    elif azione == "APRI":
        scelta = input("Vuoi caricare da file 'JSON', 'TXT' o usare i dati di 'DEFAULT'? ").strip().upper()
        if scelta == "DEFAULT":
            rubrica = Rubrica(dati_rubrica)
            print("Rubrica predefinita caricata correttamente.")
        elif scelta == "JSON":
            nome_file = input("Nome del file JSON (es. rubrica.json): ")
            rubrica = Rubrica.apri_da_json(nome_file)
            print("Rubrica aperta da file JSON.")
        elif scelta == "TXT":
            nome_file = input("Nome del file TXT (es. rubrica.txt): ")
            rubrica = Rubrica.apri_da_txt(nome_file)
            print("Rubrica aperta da file di testo.")
        else:
            print("Scelta di caricamento non valida.")

    elif azione == "AGGIUNGI":
        nome = input("Inserisci Nome e Cognome: ")
        giorno = int(input("Inserisci giorno di nascita: "))
        mese = input("Inserisci mese di nascita: ")
        anno = int(input("Inserisci anno di nascita: "))
        eta = int(input("Inserisci età: "))
        sesso = input("Inserisci sesso (M/F): ")
        mail = input("Inserisci indirizzo mail: ")

        nuovo_contatto = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }
        rubrica.aggiungi(nome, nuovo_contatto)

    elif azione == "RIMUOVI":
        nome = input("Inserisci il nome del contatto da rimuovere: ")
        rubrica.rimuovi(nome)

    elif azione == "SALVA":
        nome_file = input("Inserisci il nome del file su cui salvare (es. rubrica.json o rubrica.txt): ")
        rubrica.salva(nome_file)

    elif azione == "STAMPA":
        nome = input("Inserisci il nome del contatto da stampare: ")
        rubrica.stampa(nome)

    else:
        print("Operazione non esistente. Riprova.")