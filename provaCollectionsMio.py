import copy
from collections import Counter, deque

from gestionale.core.clienti import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1= ProdottoRecord("Laptop", 1200.0)
p2= ProdottoRecord("Mouse", 20.0)
p3= ProdottoRecord("Auricolari", 250.0)

carrello=[p1,p2,p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello: ")
for i,p in enumerate(carrello):
    print (f"{i}. {p.name}-{p.prezzo_unitario}")


#Aggiungere una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key=lambda x: x.prezzo_unitario) #se volessi ordinarsi al contrario aggiungo reverse=True
print("Prodotti nel carrello: ")
for i,p in enumerate(carrello):
    print(f"{i}. {p.name}-{p.prezzo_unitario}")

tot= sum(p.prezzo_unitario for p in carrello)
print(f"Total prezzo: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Prodotto", 100.0))
carrello.extend([ProdottoRecord("iPad", 700.0),ProdottoRecord("iPad Pro", 900.0)])
carrello.insert(2, ProdottoRecord("iPad Pro Max", 1000.0)) #questo inserisce in una posizione specifica

#per rimuovere
carrello.pop() #rimuove l'ultimo elemento
#può ammettere un argomento
carrello.pop() #rimuove l'elemento in posizione 2
carrello.remove(p1) #elimina la prima occorrenza di p1
#carrello.clear() #rimuove tutti gli elementi

#SORTING
#carrello.sort() #usa l'ordinamneto naturale della lsita ---questo non funziona se gli oggetti contenuti non contengono un metodo lt
#carrello.sort(reverse=True) #ordina al contrario
#carrello.sort(key= function)  #uso una chiave  con una funz es lambda
#carrello_ordinato= sorted(carrello)

carrello.reverse()  #restituisce la lista al contrario - dall'ultimo al primo
carrello_copia=carrello.copy()  #shallow copy -  2 liste diverse che contengono gli stessi oggetti
carrello_copia2=copy.deepcopy(carrello) # deep copy- crea la copia della lista ma anche di tutto quello che c'è dentro


#TUPLE
sede_principale=(45, 8) #latitudine e longitudine  sede ti torino
sede_milano=(45, 9) #lat e long sede

print(f"Sede principale lat: {sede_principale[0]}, long:{sede_principale[1]}")

AliquotaIVA=(
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquotaIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    """" Restituisce pezzo tot, medio, massimo e minimo"""
    prezzi=[p.prezzo_unitario for p in carrello]
    return(sum(prezzi), sum(prezzi)/len(prezzi),max(prezzi), min(prezzi))

tot, media, max, min= calcola_statistiche_carrello(carrello)

#tot, *altri_campi=calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie={"Gold", "Silver", "Bronze", "Gold"} #anche se ho un duplicato, lui li elimina e tine solo 1 copia
print(categorie)
print(f"num catgorie:{ len(categorie)}")
categorie2={"Platinum", "Elite", "Gold"}
#categorie_all=categorie.union(categorie2) #così unisco il tutto
categorie_all= categorie | categorie2 #UNIONE
print(categorie_all)

categorie_comuni=categorie & categorie2 #solo elementi comuni
print(f"Categorie comuni:{ categorie_comuni}")

categorie_esclusive= categorie-categorie2 #solo elem presenti in uno dei 2
print(f"Categorie esclusive:{ categorie_esclusive}")

categorie_esclusive_symm= categorie^categorie2 #differenza simmetrica
print(f"Categorie escl simmetriche:{ categorie_esclusive_symm}")

prodotti_ordine_A={ProdottoRecord("Laptop", 1200.0),
                   ProdottoRecord("Mouse", 20.0),
                   ProdottoRecord("Tablet", 700.0)}

prodotti_ordine_B={ProdottoRecord("Laptop2", 1200.0),
                   ProdottoRecord("Mouse2", 20.0),
                   ProdottoRecord("Tablet2", 700.0)}

#mMETODI UTILI PER I SET
s=set()
s1=set()
s.add(ProdottoRecord("aaa", 20.0))  #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #AGGIUNGO PIù ELEMENTI

#PER TOGLIERE
#s.remove(elem) #rimuove un element. Se non esiste l'ogg solleva un KeyError
#s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste
#s.pop() #rimuove e restituisce un elemento
#s.clear() #svuota il set

#OPERAZIONI INSIEMISTICHE
s.union(s1) #s | s1 unione e genera un altro set
s.intersection(s1) # s & s1 ovvero ritaglia elementi comuni
s.difference(s1)  #s-s1, ovvero elementi di s che non sono contenuti in s1
#s.symmetric_differece(s1) #s^s1, ovvero elementi si s non contenuti in s1 ed  elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi


#DICTIONARY
catalogo= {
    "LAP001": ProdottoRecord("Laptop", 1200.0),
    "LAP002": ProdottoRecord("Laptop", 2300.0),
    "MAU003":ProdottoRecord("Mouse", 1200.0),
    "AUR001":ProdottoRecord("Auricolari", 250.0)
}

cod="LAP002"
prod=catalogo[cod] #COSì VADO A RIPESCARE L'OGGETTO DAL CODICE complessi (o1)

print(f"Il prodotto con codice {cod} è {prod}")

#print(f"Cerco un altro oggetto:{catalogo["non esiste"]}") #CERCO UNA CHIAVE CHE NON ESISTE

prod1=catalogo.get("Non esiste")

if prod1 is None:
    print(" Prodotto Non trovato")

prod2=catalogo.get("Non esiste2", ProdottoRecord("Sconosciuto", 0.0)) #così se non trova stampa un ogg vuoto
print(prod2)

#CICLARE SUL DIZIONARIO
keys=list(catalogo.keys()) #COSì RECUPER LE CHIAVI
values=list(catalogo.values() )#COSì RECUPERO I VALORI

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod;{key}è associata a: {val}")

#RIMUOVERE DAL DIZIONARIO
rimossso=catalogo.pop("LAP002")
print(rimossso)

#DICT COMPREHESION
prezzi={codice: prod.prezzo_unitario for codice, prod in catalogo.items()} #credo un diz e il ciclo mi dice già come costruirlo
print(prezzi)

#DA RICORDARE PER DICT

#d[key]=v #scrivo sul dizionario
#v=d[key] #leggere-- restituisce key error se non esiste
#v=d.get(key, default) #legge senza mischiare gli error, se non esiste prende il default
#d.pop(key) #restituisce un valore e lo cancella
#d.clear() #cancella tutto
#d.keys() #mi restituisce tutte le chiavi definite nel dizionario
#d.values() #mi restituisce tutti i  valori salvati nel dizionario
#d.items() #restituisce le coppie

#key in d #condizione che verifica se key p presente del diz

""" ESERCIZIO LIVE
Per ciascuno dei seguenti casi, decidere che struttura usare"""
""" 1) Memorizzare un elenco di ordini che dovranno poi essere processati in ordine di arrivo"""
#LISTA
ordini_da_processare=[]
o1=Ordine([],ClienteRecord("Mario Rossi", "mail@polito.it", "Gold"))
o2=Ordine([],ClienteRecord("Carlo verdi", "mail@polito.it", "Bronze"))
o3=Ordine([],ClienteRecord("Fulvio Bianchi", "mail@polito.it", "Silver"))

ordini_da_processare.append(o1)
ordini_da_processare.append(o2, 10)
ordini_da_processare.append(o3, 3)

"""2) Memorizzare i CF dei Clienti (univoco)"""
#SET
codici_fiscali= {"ABGHNXFNV", "ASGBXJZDBG","AKFJMXDJ"}
#se inserisco la stessa stringa 2 volte, ne considera solo 1

"""3) Crere un database di prodotti che posso cercare con un codice univoco"""
#DIZIONARIO -va bene quando voglio cercare in maniera algoritmicamente efficiente
listino_prodotti={"LAP001":ProdottoRecord("Laptop2", 1200.0),
                  "KEY001":ProdottoRecord("Key001", 1200.0)
                  }
""" 4) Memorizzare le coord gps della nuova sede di Roma"""
#TUPLA
coord=(1,2)
"""5) Tenere delle categorie di clienti che hanno fatto un ordine in un certo range temporale"""
#LISTA O SET? Entrambi i casi andrebbero bene, ma il set è meglio così ho le categorie distinte
categorie_periodo=set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("=======================================================")

#COUNTER
lista_clienti=[
    ClienteRecord("Mario Rossi", "mail@polito.it", "Gold"),
    ClienteRecord("Carlo verdi", "mail@polito.it", "Bronze"),
    ClienteRecord("Fulvio Bianchi", "mail@polito.it", "Silver"),
    ClienteRecord("Mario Bianchi", "mail@polito.it", "Gold"),
    ClienteRecord("Silvia Rossi", "mail@polito.it", "Silver"),
    ClienteRecord("Paola Gentile", "mail@polito.it", "Gold"),
    ClienteRecord("Sara Solari", "mail@polito.it", "Bronze"),
    ClienteRecord("Giuseppe Averta", "mail@polito.it", "Silver"),
    ClienteRecord("Fulvio Corno", "mail@polito.it", "Silver")
          ]

categorie=[c.categoria for c in lista_clienti]
categoria_counter= Counter(categorie)
print("Diatribuzione categorie clienti")
print(categoria_counter)

print(" 2 Categoria più frequente")
print(categoria_counter.most_common(2))

print("TOtale")
print(categoria_counter.total())

vendite_gennaio=Counter(
    {"Laptop":13, "Tablet":15 }
)
vendite_febbraio=Counter(
    {"Laptop":3, "Stampante":1 }
)
#SOMMO
vendite_bimestre=vendite_gennaio+vendite_febbraio #POSSO SOMMARLI e li aggrega

print(f"Vendite gennaio: {vendite_gennaio}")
print(f"Vendite febbraio: {vendite_febbraio}")

print(f"Vendite bimestre: {vendite_bimestre}")

#DIFFERENZA
print(f"Differenza di vendite:{vendite_bimestre-vendite_bimestre}")

#modificare il valore in the fly
vendite_gennaio["Laptop:"]+=4
print(f"Vendite gennaio: {vendite_gennaio}")

#metodi da RICORDARE per il counter
#c.most_common(n) RESTITUISCE GLI N ELEMENTI PIù FREQUENTI
#c.total() SOMMA DEI CONTEGGI

#Deque
print(f"=============================================================")
coda_ordini=deque()

for i in range(1,10):
    cliente=ClienteRecord(f"Cliente{i}", f"cliente{i}@polito.it","Gold")
    prodotto=ProdottoRecord(f"Prodotto{i}", 100.0*i)
    ordine=Ordine([RigaOrdine(prodotto, 1), cliente])
    coda_ordini.append(ordine)

print(f"Ordini in coda:{len(coda_ordini)}")

while coda_ordini:
    odine_corrente=coda_ordini.popleft() #mi da l'ultimo inserito
    print(f"Sto gestendo l'ordine del cliente: {odine_corrente.cliente}")

print(f"Ho processato tutti gli ordini")




