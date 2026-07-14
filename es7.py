import time


# ---------------------------------------------------------------------
# Punto 1: generatore della tabellina
# ---------------------------------------------------------------------

def genera_tabellina(numero, fino_a=10):
    """Generatore: produce i valori 0*numero, 1*numero, ..., fino_a*numero
    uno alla volta (yield), invece di costruire subito tutta la lista."""
    for moltiplicatore in range(fino_a + 1):
        yield moltiplicatore * numero


# ---------------------------------------------------------------------
# Decoratore: cronometra quanto tempo impiega una partita
# ---------------------------------------------------------------------

def cronometra(funzione):
    """Decoratore: misura il tempo di esecuzione della funzione decorata,
    inoltrando tutti gli argomenti con l'unpacking *args/**kwargs
    (stesso schema visto a lezione per decorare funzioni con parametri)."""
    def wrapper(*args, **kwargs):
        inizio = time.time()
        risultato = funzione(*args, **kwargs)
        tempo_impiegato = time.time() - inizio
        print(f"\n(Tempo di gioco: {tempo_impiegato:.1f} secondi)")
        return risultato
    return wrapper


# ---------------------------------------------------------------------
# Lambda: valutazione testuale del punteggio finale
# ---------------------------------------------------------------------

valuta_punteggio = lambda punteggio, totale: (
    "Perfetto, tabellina impeccabile!" if punteggio == totale else
    "Molto bene, quasi perfetto!" if punteggio >= totale * 0.7 else
    "Continua ad esercitarti!"
)


# ---------------------------------------------------------------------
# Punto 2, 3, 4, 5: il loop di gioco
# ---------------------------------------------------------------------

COMANDI_USCITA = {"esci", "exit", "quit"}


@cronometra
def gioca_tabellina(numero, fino_a=10):
    """Ciclo principale del gioco: chiede all'utente il valore corrente
    della tabellina, uno alla volta, usando il generatore genera_tabellina.
    Gestisce input non validi (lettere, decimali, simboli) senza interrompersi,
    e un comando di uscita personalizzato."""

    generatore = genera_tabellina(numero, fino_a)
    punteggio = 0
    totale_domande = fino_a + 1

    for moltiplicatore, valore_atteso in enumerate(generatore):
        print(f"\nQuanto fa {moltiplicatore} x {numero}?")

        while True:
            risposta = input("La tua risposta (o 'esci' per uscire): ").strip()

            # Punto 5: chiusura personalizzata del gioco
            if risposta.lower() in COMANDI_USCITA:
                print(f"\nHai chiuso il gioco. Punteggio: {punteggio}/{totale_domande}")
                return punteggio

            # Punti 3+4: qualunque input non convertibile in intero
            # (lettere, simboli, numeri decimali con virgola o punto...)
            # viene gestito qui, senza interrompere il programma.
            try:
                valore_utente = int(risposta)
            except ValueError:
                print("Risposta non valida: inserisci un numero intero "
                      "(niente lettere, simboli o numeri decimali).")
                continue

            if valore_utente == valore_atteso:
                print("Corretto!")
                punteggio += 1
                break
            else:
                print(f"Sbagliato, riprova! (stai cercando {moltiplicatore} x {numero})")

    print(f"\nHai completato la tabellina del {numero}! Punteggio: {punteggio}/{totale_domande}")
    print(valuta_punteggio(punteggio, totale_domande))
    return punteggio


# ---------------------------------------------------------------------
# Input iniziale: quale tabellina giocare
# ---------------------------------------------------------------------

def chiedi_numero_tabellina():
    """Chiede all'utente quale tabellina vuole giocare, gestendo
    anche qui input non validi senza interrompere il programma."""
    while True:
        risposta = input("Che tabellina vuoi giocare? (numero intero): ").strip()
        try:
            return int(risposta)
        except ValueError:
            print("Devi inserire un numero intero valido.")


def main():
    print("=== Gioco delle tabelline ===")
    numero = chiedi_numero_tabellina()
    gioca_tabellina(numero)


if __name__ == "__main__":
    main()