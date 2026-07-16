# 
# File: es8.py
# Author: Irene De Luca 
# Date: 10/06/2026
# Version: 1.0
# Description: esercizio 8
#




# Importa il modulo 'json' per decodificare i dati nel file delle parole
import json
# Importa il modulo 'random' per estrarre casualmente la parola da indovinare
import random

# Specifica il nome del file JSON che contiene l'archivio delle parole di gioco
FILE_PAROLE = "parole.json"
# Definisce il numero massimo di errori concessi prima del game over
TENTATIVI_MAX = 6


# 
# Eccezioni personalizzate: come StopIteration, non indicano un "errore"
# ma la fine  di un'operazione, cioè del turno di gioco.
# 

# Crea una classe di eccezione personalizzata che eredita dalla classe base Exception
class ParolaIndovinata(Exception):
    """Sollevata quando il giocatore indovina l'intera parola."""
    # 'pass' serve solo come segnaposto perché l'eccezione non ha bisogno di metodi o logiche interne
    pass


# Crea un'altra classe di eccezione per gestire lo scenario di sconfitta
class TentativiEsauriti(Exception):
    """Sollevata quando finiscono i tentativi a disposizione."""
    pass


def carica_parole(percorso):
    """Legge la lista di parole da un file JSON: qui NON controlliamo
    prima le precondizioni, proviamo direttamente e gestiamo l'eccezione
    se qualcosa va storto (stile EAFP)."""

    # Inizia il primo blocco di gestione degli errori per l'apertura e la lettura del file
    try:
        # Prova direttamente ad aprire il file e caricarne il contenuto JSON
        with open(percorso, "r", encoding="utf-8") as f:
            dati = json.load(f)
    # Se il file non esiste sul disco, cattura l'eccezione FileNotFoundError
    except FileNotFoundError:
        # Avvisa l'utente della mancanza fisica del file
        print(f"Errore: il file '{percorso}' non esiste.")
        # Ritorna None per segnalare il fallimento
        return None
    # Se il file esiste ma non contiene testo in formato JSON valido, cattura JSONDecodeError
    except json.JSONDecodeError as errore:
        # Mostra il dettaglio dell'errore di formattazione del testo
        print(f"Errore: il file '{percorso}' non è un JSON valido ({errore}).")
        return None

    # Inizia un secondo blocco di controllo per verificare la presenza della chiave
    try:
        # Prova ad accedere direttamente alla chiave 'parole' del dizionario
        lista_parole = dati["parole"]
    # Se la chiave 'parole' non esiste nel dizionario, Python solleva un KeyError
    except KeyError:
        # Cattura il KeyError e avvisa l'utente della struttura JSON non conforme
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None

    # Inizia il terzo blocco di controllo per estrarre la parola casuale
    try:
        # Tenta di estrarre a caso una parola dalla lista e di convertirla in minuscolo
        return random.choice(lista_parole).lower()
    # Se la lista di parole è vuota, random.choice solleva un errore di indice (IndexError)
    except IndexError:
        # Cattura l'IndexError per segnalare che non ci sono parole utilizzabili nel file
        print("Errore: la lista delle parole è vuota.")
        return None


def costruisci_posizioni(parola):
    """Costruisce un dizionario {lettera: [indici]} usando lo stesso
    identico schema EAFP della dispensa per riempire un dizionario:
    proviamo ad aggiungere all'indice esistente, e se la chiave non
    c'è ancora, catturiamo il KeyError e la creiamo."""
    # Inizializza un dizionario vuoto che conterrà le lettere come chiavi e la lista delle loro posizioni come valore
    posizioni = {}
    # Scorre la parola fornendo contemporaneamente l'indice numerico e la lettera (carattere)
    for indice, carattere in enumerate(parola):
        # Tenta l'approccio ottimistico: assume che la lettera sia già presente nel dizionario
        try:
            # Prova ad appendere l'indice corrente alla lista associata a quella lettera
            posizioni[carattere].append(indice)
        # Se la lettera viene incontrata per la prima volta, l'accesso solleva un KeyError
        except KeyError:
            # Intercetta il KeyError e crea la lista da zero inserendovi il primo indice trovato
            posizioni[carattere] = [indice]
    # Restituisce il dizionario delle posizioni mappate (es. "mamma" -> {'m': [0, 2, 3], 'a': [1, 4]})
    return posizioni


def mostra_stato(parola, posizioni_rivelate, lettere_tentate, tentativi_rimasti):
    """Stampa lo stato corrente del gioco."""
    # Ricostruisce la parola oscurata: mostra la lettera reale se il suo indice è presente tra le posizioni rivelate,
    # altrimenti mostra un trattino basso '_'. Unisce il tutto con uno spazio.
    mascherata = " ".join(
        carattere if indice in posizioni_rivelate else "_"
        for indice, carattere in enumerate(parola)
    )
    # Mostra la parola formattata a schermo
    print(f"\nParola: {mascherata}")
    # Mostra i tentativi residui prima della sconfitta
    print(f"Tentativi rimasti: {tentativi_rimasti}")
    # Stampa le lettere già tentate ordinate alfabeticamente. Se il dizionario è vuoto, usa l'operatore 'or' per mostrare '(nessuna)'
    print(f"Lettere già tentate: {', '.join(sorted(lettere_tentate)) or '(nessuna)'}")


def gioca(parola):
    """Ciclo principale del gioco, in stile EAFP: proviamo direttamente
    le operazioni e gestiamo le eccezioni, invece di controllare prima."""

    # Costruisce la mappa delle posizioni dei caratteri della parola
    posizioni = costruisci_posizioni(parola)
    # Crea un dizionario vuoto che useremo per memorizzare le lettere tentate (sfruttando le eccezioni sulle sue chiavi)
    lettere_tentate = {}          
    # Crea un set vuoto per tenere traccia degli indici delle lettere indovinate e mostrate a schermo
    posizioni_rivelate = set()
    # Imposta il conteggio iniziale dei tentativi
    tentativi_rimasti = TENTATIVI_MAX

    # Blocco try principale che racchiude l'intero ciclo di gioco. Serve a catturare le eccezioni di vittoria/sconfitta.
    try:
        # Avvia un ciclo di gioco infinito che continuerà finché non verrà sollevata un'eccezione di fine partita
        while True:
            # Mostra la situazione di gioco aggiornata
            mostra_stato(parola, posizioni_rivelate, lettere_tentate, tentativi_rimasti)
            # Acquisisce l'input, pulisce gli spazi ed uniforma in caratteri minuscoli
            guess = input("Inserisci una lettera o prova l'intera parola: ").strip().lower()

            # Un sotto-blocco try per catturare e gestire lo stato di ogni singolo inserimento
            try:
                # Controlla se l'input inserito è lungo esattamente un carattere
                if len(guess) == 1:
                    # --- guess di una singola lettera ---
                    # Tenta di accedere alla lettera nel dizionario lettere_tentate per verificare se è già stata inserita
                    try:
                        lettere_tentate[guess]  # Se la chiave esiste, non succede nulla e si passa al ramo "else" del blocco try
                    # Se la chiave non esiste, significa che la lettera non è mai stata provata prima
                    except KeyError:
                        # Registra la nuova lettera nel dizionario delle lettere tentate impostando il valore a True
                        lettere_tentate[guess] = True
                        # Tenta di recuperare la lista degli indici in cui compare questa lettera nella parola
                        try:
                            indici = posizioni[guess]
                        # Se la lettera non è presente nella parola, la chiave nel dizionario "posizioni" non esiste (KeyError)
                        except KeyError:
                            # Riduce di 1 i tentativi rimasti per via dell'errore
                            tentativi_rimasti -= 1
                            # Notifica all'utente che la lettera non è presente
                            print("Lettera sbagliata!")
                        # Se la chiave esiste nel dizionario delle posizioni, esegue questo blocco (nessuna eccezione sollevata)
                        else:
                            # Aggiorna l'insieme delle posizioni rivelate inserendo i nuovi indici indovinati
                            posizioni_rivelate.update(indici)
                            # Notifica l'esito positivo
                            print("Lettera corretta!")
                    # Questo blocco viene eseguito solo se la prima operazione (lettere_tentate[guess]) ha avuto successo senza KeyError
                    else:
                        # Segnala all'utente che ha inserito un duplicato inutile
                        print(f"Hai già provato la lettera '{guess}'.")

                # Se la stringa inserita ha una lunghezza diversa da 1, viene considerata come un tentativo di indovinare la parola intera
                else:
                    # --- guess dell'intera parola ---
                    # Controlla se la parola digitata corrisponde esattamente a quella segreta
                    if guess == parola:
                        # Se è corretta, solleva l'eccezione personalizzata di vittoria
                        raise ParolaIndovinata
                    # Se la parola inserita è sbagliata
                    else:
                        # Sottrae un tentativo a quelli a disposizione
                        tentativi_rimasti -= 1
                        # Notifica l'errore
                        print("Parola sbagliata!")

                # Al termine del turno, verifica se il numero di indici rivelati è pari alla lunghezza totale della parola
                if len(posizioni_rivelate) == len(parola):
                    # Se tutte le lettere sono scoperte, solleva l'eccezione di vittoria
                    raise ParolaIndovinata
                # Verifica se i tentativi a disposizione sono terminati
                if tentativi_rimasti <= 0:
                    # Solleva l'eccezione di sconfitta per interrompere il gioco
                    raise TentativiEsauriti

            # Il blocco 'finally' viene eseguito SEMPRE alla fine di ogni iterazione del ciclo, 
            # sia in caso di inserimento corretto, sia in caso di errore, sia prima che le eccezioni vengano propagate.
            finally:
                # Stampa un separatore grafico di fine turno
                print("--- fine turno ---")

    # Cattura l'eccezione di vittoria sollevata all'interno del ciclo di gioco
    except ParolaIndovinata:
        # Mostra il messaggio di vittoria e rivela la parola corretta
        print(f"\nHai indovinato! La parola era '{parola}'.")
    # Cattura l'eccezione di sconfitta sollevata all'interno del ciclo
    except TentativiEsauriti:
        # Comunica il game over e mostra la parola corretta
        print(f"\nHai esaurito i tentativi. La parola era '{parola}'.")


def main():
    # Carica in maniera sicura ed in stile EAFP la parola misteriosa tramite la funzione dedicata
    parola = carica_parole(FILE_PAROLE)

    # qui un semplice controllo sul valore di ritorno non è una violazione
    # dello stile EAFP: la gestione delle eccezioni vere e proprie è già
    # avvenuta dentro carica_parole()
    if parola is None:
        # Se non è stato possibile ricavare una parola, interrompe l'esecuzione dello script
        print("Impossibile avviare il gioco.")
        # Esce dalla funzione principale
        return

    # Avvia la partita vera e propria passando la parola caricata
    gioca(parola)


# Idioma standard per garantire l'avvio del codice solo in caso di esecuzione diretta del file
if __name__ == "__main__":
    main()