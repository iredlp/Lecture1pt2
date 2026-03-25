import copy

from gestionale.core.prodotti import ProdottoRecord

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
s.symmetric_differece(s1) #s^s1, ovvero elementi si s non contenuti in s1 ed  elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi

