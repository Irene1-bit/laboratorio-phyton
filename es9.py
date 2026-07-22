# 
# File: es9.py
# Author: Irene De Luca 
# Date: 26cle/06/2026
# Version: 1.0
# Description: esercizio 9
#




import argparse  # Gestisce l'analisi degli argomenti passati da riga di comando (CLI)
import random  # Consente di estrarre caratteri casuali e mescolare liste
import string  # Fornisce gruppi di caratteri predefiniti (lettere, cifre, ecc.)


# ECCEZIONI PERSONALIZZATE 


class CriteriaError(Exception):
    """Sollevata quando i criteri richiesti per la password sono impossibili da soddisfare."""

    pass  # Segnaposto per definire una classe di eccezione vuota


#  GENERAZIONE PASSWORD 


def genera_password(lunghezza=12, maiuscole=True, numeri=True, simboli=True):
    """Genera una password casuale rispettando i criteri richiesti."""
    # Inizializza il pool di caratteri partendo dalle lettere minuscole
    pool = list(string.ascii_lowercase)
    # Lista per raccogliere almeno un carattere per ciascuna categoria richiesta
    obbligatori = []

    # Se richiesto, aggiunge le maiuscole al pool e ne sceglie una obbligatoria
    if maiuscole:
        pool += list(string.ascii_uppercase)
        obbligatori.append(random.choice(string.ascii_uppercase))

    # Se richiesto, aggiunge i numeri al pool e ne sceglie uno obbligatorio
    if numeri:
        pool += list(string.digits)
        obbligatori.append(random.choice(string.digits))

    # Se richiesto, aggiunge i simboli al pool e ne sceglie uno obbligatorio
    if simboli:
        simboli_ammessi = "!@#$%&*?+-"
        pool += list(simboli_ammessi)
        obbligatori.append(random.choice(simboli_ammessi))

    # CONTROLLO LBYL: Verifica se la lunghezza è sufficiente per i caratteri obbligatori
    if lunghezza < len(obbligatori):
        raise CriteriaError(f"Lunghezza {lunghezza} troppo corta! Servono almeno {len(obbligatori)} caratteri.")

    # Completa il resto della password con caratteri casuali dal pool
    resto = [random.choice(pool) for _ in range(lunghezza - len(obbligatori))]

    # Unisce i caratteri obbligatori con il resto e li mescola casualmente
    caratteri = obbligatori + resto
    random.shuffle(caratteri)

    # Converte la lista di caratteri in una stringa finale
    return "".join(caratteri)


# VALUTAZIONE E ROBUSTEZZA 

# Dizionario contenente i criteri di valutazione espresso tramite funzioni lambda
CRITERI = {
    # Chiave "lunghezza >= 8": controlla se len(p) è maggiore o uguale a 8
    "lunghezza >= 8": lambda p: len(p) >= 8,
    # Chiave "lunghezza >= 12": controlla se len(p) è maggiore o uguale a 12
    "lunghezza >= 12": lambda p: len(p) >= 12,
    # Scorre la password 'p' e verifica se c'è almeno una lettera minuscola (c.islower())
    "contiene minuscole": lambda p: any(c.islower() for c in p),
    # Scorre la password 'p' e verifica se c'è almeno una lettera maiuscola (c.isupper())
    "contiene maiuscole": lambda p: any(c.isupper() for c in p),
    # Scorre la password 'p' e verifica se c'è almeno un numero (c.isdigit())
    "contiene numeri": lambda p: any(c.isdigit() for c in p),
    # Scorre 'p' e verifica se almeno un carattere appartiene alla stringa di simboli
    "contiene simboli": lambda p: any(c in "!@#$%&*?+-_." for c in p),
    # Verifica tramite 'not in' che non ci siano spazi vuoti nella password 'p'
    "nessuno spazio": lambda p: " " not in p,
}


def valuta_password(password):
    """Applica tutti i criteri e restituisce il punteggio e il dettaglio dei controlli."""
    # Esegue ogni funzione lambda del dizionario sulla password fornita
    dettagli = {nome: func(password) for nome, func in CRITERI.items()}
    # Somma i risultati booleani (True = 1, False = 0) per calcolare il punteggio
    punteggio = sum(dettagli.values())
    return punteggio, dettagli


def valutazione_testuale(punteggio, totale_criteri):
    """Converte il punteggio numerico in un giudizio leggibile."""
    percentuale = punteggio / totale_criteri

    if percentuale == 1.0:
        return "Eccellente"
    elif percentuale >= 0.7:
        return "Forte"
    elif percentuale >= 0.4:
        return "Media"
    else:
        return "Debole"


# INTERFACCIA DA RIGA DI COMANDO 


def crea_parser():
    """Configura e restituisce il parser per i comandi da terminale."""
    parser = argparse.ArgumentParser(
        description="Password: Generatore e verificatore di password."
    )

    # Argomento per generare una password
    parser.add_argument(
        "-g",
        "--genera",
        action="store_true",
        help="Genera una nuova password casuale",
    )
    # Argomento per verificare una password esistente
    parser.add_argument(
        "-v",
        "--verifica",
        type=str,
        help="Verifica la robustezza di una password specifica",
    )
    # Opzioni di configurazione per la generazione
    parser.add_argument(
        "-l",
        "--lunghezza",
        type=int,
        default=12,
        help="Lunghezza della password (default: 12)",
    )
    parser.add_argument(
        "--no-maiuscole", action="store_true", help="Esclude le lettere maiuscole"
    )
    parser.add_argument(
        "--no-numeri", action="store_true", help="Esclude i numeri"
    )
    parser.add_argument(
        "--no-simboli", action="store_true", help="Esclude i simboli speciali"
    )

    return parser


def main():
    """Funzione principale che gestisce la logica di avvio."""
    # Configura il parser per i comandi da terminale
    parser = crea_parser()
    # Legge ed estrae gli argomenti effettivi passati dall'utente
    args = parser.parse_args()

    # CASO 1: L'utente vuole GENERARE una password (ha inserito -g o --genera)
    if args.genera:
        try: # Inizia un blocco protetto per catturare eventuali errori di configurazione
            # Genera la password invertendo le opzioni 'no-*' con l'operatore 'not'
            pwd = genera_password(
                lunghezza=args.lunghezza,
                maiuscole=not args.no_maiuscole,
                numeri=not args.no_numeri,
                simboli=not args.no_simboli,
            )
            # Calcola il punteggio della password ignorando i dettagli (usando '_')
            punteggio, _ = valuta_password(pwd)
            # Converte il punteggio in un giudizio testuale (es. "Forte", "Eccellente")
            giudizio = valutazione_testuale(punteggio, len(CRITERI))

            # Stampa la password generata e la sua valutazione
            print(f"\nPassword Generata: {pwd}")
            print(f"Robustezza:        {giudizio} ({punteggio}/{len(CRITERI)})\n")

        # Intercetta l'eccezione se i criteri richiesti sono impossibili da soddisfare
        except CriteriaError as e:
            # Stampa il messaggio di errore personalizzato senza far crashare il programma
            print(f"\nErrore di configurazione: {e}\n")

    # CASO 2: L'utente vuole VERIFICARE una password esistente
    elif args.verifica:
        punteggio, dettagli = valuta_password(args.verifica)
        giudizio = valutazione_testuale(punteggio, len(CRITERI))

        print(f"\nPassword analizzata: {args.verifica}")
        print(
            f"Giudizio globale:   {giudizio} ({punteggio}/{len(CRITERI)} criteri superati)\n"
        )
        print("Dettaglio controlli:")
        for nome, ok in dettagli.items():
            simbolo = "OK" if ok else "X "
            print(f"  [{simbolo}] {nome}")
        print()

    # CASO 3: L'utente non ha specificato comandi
    else:
        parser.print_help()


# Avvio dello script
if __name__ == "__main__":
    main()