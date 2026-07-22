#
#File:esercizio2.py
#
#Author:Irene De Luca
#
#Date:22/03/2026
#
#Version:1.0
#
#Description:Esercizio 2

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

#punt1 
'conto le righe non vuote'
righe = testo.split("\n")          #divide il testo in righe ogni volta che andiamo a capo
righe_non_vuote = [r for r in righe if r.strip() !=""]      #elimina le righe vuote usando la list comprehension, orima elimina gli spazi, se non rimane nulla la elimina
print (len(righe_non_vuote))         #stampa il numero di righe non vuote
 
input("premi invio per continuare")
#punto 2 
'conto le parole'
parole=testo.split ()       #divide il testo in parole in bae agli spazi
print(len(parole))

input("premi invio per continuare")

#punt 3 
'conto i caratteri alfanumerici'
conta =0    #inizializza contatore partendo da zero
for c in testo:     #assegna ai caratteri la variabile c
    if c.isalnum():     #controlla se è lettera o è numero
        conta +=1       #incrementa il contatore
print(conta)

input("premi invio per continuare")

#punto4 
'conto una lettera a scelta'
lettera=input("dimmi un lettera: ")     #chiede una lettera come input
conteggio =0    #inizializza un contatore da zero
for c in testo:     
    if c.lower() ==lettera.lower():     #confronta ignorando maiuscole e minoscole
        conteggio+=1

print(conteggio)

input("premi invio per continuare")

#punto5 
'sostiuisco con PYTHON '
testo_mod =testo.lower()         #porta tutto minuscolo e salva in una nuova variabile
testo_mod=testo_mod.replace ("day", "PYTHON")
testo_mod=testo_mod.replace ("water", "PYTHON")
testo_mod=testo_mod.replace ("about", "PYTHON")

print (testo_mod)

input("premi invio per continuare")


#punto6
'sostituisco le parole in posizione dispari in maiuscolo'
parole= testo.split()
for i in range (len(parole)):
    if i % 2==1:        #posizione dispari
        parole [i]=parole[i].upper()

nuovo_testo=" ".join(parole)     #prende gli elementi da parole e li unisce separandoli con uno spazio
print(nuovo_testo)


input("premi invio per continuare")



#punto7
'inverto ordine delle righe'
righe=testo.strip().split("\n")     #rimuove gli spazi iniziali e finali e divide ogni volta che va a capo
righe_invertite=righe[::-1]     #slicing per invertire la lista, utilizzo -1 per invertire

print("\n".join(righe_invertite))       #ricompone il testo inserendo il a capo


input("premi invio per continuare")


#punto 8
'scrivo il secondo verso di ogni strofa a specchio'
strofe= testo.strip().split("\n\n")     #divide per strofe
risultato=[]



for strofa in strofe:               #scorre una strofa alla volta
    versi=strofa.split("\n")        #divide la strofa in versi

    if len(versi) >1:
        versi[1]=versi[1][::-1]     #inverte il secondo verso, perche parte da zero, e lo inverte

        risultato.append("\n".join(versi)) #riunisce tutto insieme e separa con uno spazio, e aggiunge alla lista risultato

print ("\n\n".join(risultato))


input("premi invio per continuare")


#punto9
strofe = testo.lower().split("\n\n")
insiemi = []

for strofa in strofe:
    # Rimuoviamo la punteggiatura per evitare che "ocean." o "christ!" sballino il conteggio
    for carattere in [',', '.', ';', ':', '!', '?']:
        strofa = strofa.replace(carattere, '') #lo trasforma in uno spazio
    parole = set(strofa.split()) #mette in un set che elimina i duplicati
    insiemi.append(parole) #aggiunge alla fine di insiemi la lista di parole

# Intersezione di tutti i set
comuni = set.intersection(*insiemi)     #trova gli elementi in intersezione tra tutti gli insiemi 

# Controlliamo se il set 'comuni' contiene qualcosa
if len(comuni) > 0:
    print(f"Le parole presenti in tutte le strofe sono: {comuni}")
else:
    print("Non ci sono parole comuni a tutte le strofe")




input("premi invio per continuare")


#punto 10
'lista univoca di parole ordinata per lunghezza'
parole=testo.lower().split()
uniche=list(set(parole))        #rimuove duplicati mettendole nel set

uniche.sort(key=len)        #ordina per lunghezza parola
print (uniche)



input("premi invio per continuare")


#punto11

diz= {}     #crea dizionario vuoto

for c in testo:    # scorre il testo e asssegna la variabile 
    if c in diz:    #se c è gia nel dizionario incrfementa di uno
        diz[c] +=1
    else:
        diz[c]=1        #se non c'è le assegna il valore 1
print(diz)


input("premi invio per continuare")




#punto 12

diz2 ={}        #stessa logica del punto prima ma vede che sia carattere, numero
for c in testo.lower():
    if c.isalnum():
        if c in diz2:
            diz2[c]+=1
        else:
            diz2[c]=1
print(diz2)