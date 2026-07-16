# 
# File: es6.py
# Author: Irene De Luca 
# Date: 28/05/2026
# Version: 1.0
# Description: esercizio 6
#

# Importa il modulo integrato di Python per gestire i file in formato JSON (JavaScript Object Notation)
import json


# 1. DEFINIZIONE DELLA CLASSE RUBRICA


# Definisce la classe "Rubrica", il modello (blueprint) per creare i nostri oggetti rubrica
class Rubrica:
    """Una classe per gestire una rubrica telefonica con i dati dei contatti"""

    # Il costruttore della classe. Inizializza l'oggetto quando viene creato.
    # Accetta un dizionario iniziale facoltativo (il cui valore predefinito è None).
    def __init__(self, dizionario_iniziale=None):
        """Inizializza la rubrica con un dizionario"""
        # Salva il dizionario passato come argomento all'interno dell'attributo di istanza "self.contatti"
        self.contatti = dizionario_iniziale

    # Decoratore che definisce un metodo di classe. Riceve la classe stessa (cls) invece dell'istanza (self).
    @classmethod
    def apri_da_json(cls, nome_file):
        """Inizializza la rubrica leggendo da un file JSON"""
        # Apre il file specificato in modalità lettura ('r') usando un contesto sicuro "with" (che chiude il file in automatico)
        with open(nome_file, 'r') as f:
            # Carica il contenuto del file JSON e lo converte in un dizionario Python
            dati = json.load(f)
        # Crea e restituisce una nuova istanza della classe Rubrica (usando cls) pre-popolata con i dati letti
        return cls(dati)

    # Altro metodo di classe per inizializzare la rubrica a partire da un file di testo semplice (.txt)
    @classmethod
    def apri_da_txt(cls, nome_file):
        """Inizializza la rubrica leggendo da un file di testo"""
        # Apre il file di testo specificato in modalità lettura ('r')
        with open(nome_file, 'r') as f:
            # Legge l'intero contenuto del file come se fosse una stringa di testo unica
            contenuto = f.read()
            # eval() valuta la stringa come codice Python. In questo caso, converte la stringa di un dizionario in un vero dizionario Python.
            # Nota: eval() è potente ma rischioso se il file txt contiene codice maligno.
            dati = eval(contenuto)
        # Crea e restituisce una nuova istanza della classe Rubrica popolata con i dati convertiti
        return cls(dati)

    # Metodo d'istanza per aggiungere o aggiornare un contatto nella rubrica
    def aggiungi(self, nome, dati_contatto):
        """Aggiunge un elemento alla rubrica"""
        # Controlla se la rubrica non è ancora stata inizializzata con un dizionario (cioè è ancora None)
        if self.contatti is None:
            # Mostra un messaggio di avviso all'utente
            print("Prima apri una rubrica")
            # Interrompe l'esecuzione del metodo senza fare nulla
            return
        # Associa il nome del contatto (chiave) al dizionario contenente i suoi dati (valore)
        self.contatti[nome] = dati_contatto

    # Metodo d'istanza per eliminare un contatto dalla rubrica cercando per nome
    def rimuovi(self, nome):
        """Rimuove un elemento dalla rubrica dato il nome"""
        # Controlla se la rubrica non esiste (None) oppure se il dizionario dei contatti è vuoto (lunghezza pari a 0)
        if self.contatti is None or len(self.contatti) == 0:
            # Avvisa l'utente che non c'è nulla da rimuovere
            print("La rubrica è vuota.")
            # Interrompe il metodo
            return
        # Controlla se il nome inserito non è presente tra le chiavi del dizionario dei contatti
        if nome not in self.contatti:
            # Avvisa l'utente che il contatto cercato non esiste
            print(f"Il contatto {nome} non esiste in rubrica")
            # Interrompe il metodo
            return
        # Rimuove fisicamente la coppia chiave-valore corrispondente al nome dal dizionario dei contatti
        del self.contatti[nome]

    # Metodo d'istanza per mostrare a schermo le informazioni dettagliate di un singolo contatto
    def stampa(self, nome):
        """Stampa tutte le informazioni di un contatto dato il nome"""
        # Controlla se la rubrica non esiste o è vuota
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota.")
            return
        # Controlla se il nome inserito non è presente in rubrica
        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return
        
        # Recupera il dizionario dei dettagli associato a quel nome specifico
        contatto = self.contatti[nome]
        # Stampa il nome del contatto
        print(f"Nome: {nome}")
        # Stampa la data di nascita formattata estraendo giorno, mese e anno dal dizionario dei dettagli
        print(f"Nato il: {contatto['giorno']} {contatto['mese']} {contatto['anno']}")
        # Stampa l'età recuperandola dalla chiave 'età'
        print(f"Età: {contatto['età']}")
        # Stampa il sesso recuperandolo dalla chiave 'sesso'
        print(f"Sesso: {contatto['sesso']}")
        # Stampa l'indirizzo email recuperandolo dalla chiave 'mail'
        print(f"Mail: {contatto['mail']}")

    # Metodo d'istanza per salvare lo stato attuale della rubrica su un file
    def salva(self, nome_file):
        """Salva la rubrica su file JSON o TXT"""
        # Controlla se non ci sono contatti da salvare
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota")
            return

        # Verifica se l'utente ha inserito un nome di file che termina con l'estensione ".json"
        if nome_file.endswith(".json"):
            # Apre il file in modalità scrittura ('w'), sovrascrivendo eventuali file esistenti
            with open(nome_file, 'w') as f:
                # Scrive il dizionario dei contatti nel file in formato JSON con una formattazione leggibile (rientro di 4 spazi)
                json.dump(self.contatti, f, indent=4)
        # Se l'estensione non è .json, assume che si voglia salvare in formato di testo semplice (.txt)
        else:
            # Apre il file in modalità scrittura ('w')
            with open(nome_file, 'w') as f:
                # Converte il dizionario dei contatti in una stringa di testo e la scrive nel file
                f.write(str(self.contatti))


# ==============================================================================
# 2. PROGRAMMA INTERATTIVO PRINCIPALE
# ==============================================================================
# Definisce un dizionario di prova preconfezionato da usare come rubrica di default
dati_rubrica = {
  'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
  'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
  'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
  'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

# Inizializza un oggetto Rubrica vuoto impostando "self.contatti" su None.
# L'utente dovrà usare il comando "APRI" per popolarlo prima di poter fare altre operazioni.
rubrica = Rubrica(None)

# Avvia un ciclo infinito per l'interfaccia interattiva a riga di comando
while True:
    # Chiede all'utente quale azione vuole compiere.
    # .strip() rimuove eventuali spazi bianchi superflui all'inizio/fine dell'input.
    # .upper() converte tutto in maiuscolo per evitare problemi di case-sensitivity (es. "apri" diventa "APRI").
    azione = input("\nInserisci l'azione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA) o 'EXIT': ").strip().upper()

    # Se l'utente digita "EXIT", il programma saluta e interrompe il ciclo infinito
    if azione == "EXIT":
        print("Programma terminato.")
        break

    # Se l'utente sceglie di inizializzare o caricare una rubrica
    elif azione == "APRI":
        # Chiede da dove caricare i dati dei contatti
        scelta = input("Vuoi caricare da file 'JSON', 'TXT' o usare i dati di 'DEFAULT'? ").strip().upper()
        # Se sceglie la rubrica predefinita
        if scelta == "DEFAULT":
            # Crea un nuovo oggetto Rubrica passando il dizionario "dati_rubrica" definito poche righe sopra
            rubrica = Rubrica(dati_rubrica)
            print("Rubrica predefinita caricata correttamente.")
        # Se sceglie di importare da un file JSON
        elif scelta == "JSON":
            # Chiede all'utente il percorso/nome del file da leggere
            nome_file = input("Nome del file JSON (es. rubrica.json): ")
            # Chiama il metodo di classe per leggere il JSON e assegna il nuovo oggetto alla variabile "rubrica"
            rubrica = Rubrica.apri_da_json(nome_file)
            print("Rubrica aperta da file JSON.")
        # Se sceglie di importare da un file TXT
        elif scelta == "TXT":
            # Chiede all'utente il nome del file di testo
            nome_file = input("Nome del file TXT (es. rubrica.txt): ")
            # Chiama il metodo di classe per leggere il TXT e assegna il nuovo oggetto a "rubrica"
            rubrica = Rubrica.apri_da_txt(nome_file)
            print("Rubrica aperta da file di testo.")
        # Se l'input non corrisponde a nessuna delle tre opzioni valide
        else:
            print("Scelta di caricamento non valida.")

    # Se l'utente vuole inserire un nuovo contatto
    elif azione == "AGGIUNGI":
        # Chiede sequenzialmente in input tutti i dettagli anagrafici del nuovo contatto
        nome = input("Inserisci Nome e Cognome: ")
        # Converte l'input in intero (int) perché il giorno è un numero
        giorno = int(input("Inserisci giorno di nascita: "))
        mese = input("Inserisci mese di nascita: ")
        # Converte l'input in intero per l'anno
        anno = int(input("Inserisci anno di nascita: "))
        # Converte l'input in intero per l'età
        eta = int(input("Inserisci età: "))
        sesso = input("Inserisci sesso (M/F): ")
        mail = input("Inserisci indirizzo mail: ")

        # Costruisce il sotto-dizionario con i dati anagrafici appena inseriti
        nuovo_contatto = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }
        # Chiama il metodo "aggiungi" sull'oggetto rubrica attivo, passando il nome e il dizionario dei dati
        rubrica.aggiungi(nome, nuovo_contatto)

    # Se l'utente vuole cancellare un contatto esistente
    elif azione == "RIMUOVI":
        # Chiede il nome esatto del contatto da eliminare
        nome = input("Inserisci il nome del contatto da rimuovere: ")
        # Chiama il metodo "rimuovi" sull'oggetto rubrica
        rubrica.rimuovi(nome)

    # Se l'utente vuole salvare i dati attualmente in memoria su un file
    elif azione == "SALVA":
        # Chiede il nome del file di destinazione (es. rubrica.json o rubrica.txt)
        nome_file = input("Inserisci il nome del file su cui salvare (es. rubrica.json o rubrica.txt): ")
        # Chiama il metodo "salva" sull'oggetto rubrica per scrivere i dati su disco
        rubrica.salva(nome_file)

    # Se l'utente vuole visualizzare le informazioni di un contatto a schermo
    elif azione == "STAMPA":
        # Chiede il nome del contatto da cercare e mostrare
        nome = input("Inserisci il nome del contatto da stampare: ")
        # Chiama il metodo "stampa" che formatterà e visualizzerà i dettagli a schermo
        rubrica.stampa(nome)

    # Se l'utente inserisce un comando non riconosciuto nel menu principale
    else:
        print("Operazione non esistente. Riprova.")