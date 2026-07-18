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
righe = testo.split("\n")          #divide il testo in righe usando a capo
righe_non_vuote = [r for r in righe if r.strip() !=""]      #elimina le righe vuote
print (len(righe_non_vuote))         #stampa il numero di righe utili
 
input("premi invio per continuare")
#punto 2 
'conto le parole'
parole=testo.split ()       #divide il testo in parole
print(len(parole))

input("premi invio per continuare")

#punt 3 
'conto i caratteri alfanumerici'
conta =0
for c in testo:
    if c.isalnum():     #controlla se è lettera o è numero
        conta +=1
print(conta)

input("premi invio per continuare")

#punto4 
'conto una lettera a scelta'
lettera=input("dimmi un lettera: ")
conteggio =0
for c in testo:
    if c.lower() ==lettera.lower():     #confronta ignorando maiuscole e minoscole
        conteggio+=1

print(conteggio)

input("premi invio per continuare")

#punto5 
'sostiuisco con python alcune parole'
testo_mod =testo.lower()         #porta tutto minuscolo 
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

nuovo_testo=" ".join(parole)     #spazio tra le parole
print(nuovo_testo)


input("premi invio per continuare")



#punto7
'inverto ordine delle righe'
righe=testo.strip().split("\n")     #rimuove gli spazi iniziali e finali e divide
righe_invertite=righe[::-1]     #slicing per invertire la lista

print("\n".join(righe_invertite))       #ricompone il testo


input("premi invio per continuare")


#punto 8
'scrivo il secondo verso di ogni strofa a specchio'
strofe= testo.strip().split("\n\n")     #divide per strofe
risultato=[]



for strofa in strofe:
    versi=strofa.split("\n")        #divide la strofa in versi

    if len(versi) >1:
        versi[1]=versi[1][::-1]     #inverte il secondo verso

        risultato.append("\n".join(versi))

print ("\n\n".join(risultato))


input("premi invio per continuare")


#punto9
strofe = testo.lower().split("\n\n")
insiemi = []

for strofa in strofe:
    # Rimuoviamo la punteggiatura per evitare che "ocean." o "christ!" sballino il conteggio
    for carattere in [',', '.', ';', ':', '!', '?']:
        strofa = strofa.replace(carattere, '')
    parole = set(strofa.split())
    insiemi.append(parole)

# Intersezione di tutti i set
comuni = set.intersection(*insiemi)

# Controlliamo se il set 'comuni' contiene qualcosa
if len(comuni) > 0:
    print(f"Le parole presenti in tutte le strofe sono: {comuni}")
else:
    print("Non ci sono parole comuni a tutte le strofe")




input("premi invio per continuare")


#punto 10
'lista univoca di parole ordinata per lunghezza'
parole=testo.lower().split()
uniche=list(set(parole))        #rimuove duplicati

uniche.sort(key=len)        #ordina per lunghezza parola
print (uniche)



input("premi invio per continuare")


#punto11

diz= {}

for c in testo:
    if c in diz:
        diz[c] +=1
    else:
        diz[c]=1
print(diz)


input("premi invio per continuare")




#punto 12

diz2 ={}
for c in testo.lower():
    if c.isalnum():
        if c in diz2:
            diz2[c]+=1
        else:
            diz2[c]=1
print(diz2)