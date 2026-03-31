""""
Scrivere un software gestionle che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini
1 bis) quando arriva un nuovo ordine lo aggiungo ad una coda, assicurandomi che sia eseguito solo dopo gli altri
2) avere delle funzionalità per avere statistiche sugli ordini
3)fornire statistiche sulla distribu di ordini per categoria di cliente
"""
from collections import deque, Counter, defaultdict

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.provaCollections import ordini_da_processare
from gestionale.vendite.ordini import Ordine, RigaOrdine
from provaCollectionsMio import prodotto


class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare=deque()
        self._ordini_processati=[]
        self._statistiche_prodotti=Counter()
        self._ordini_per_categoria=defaultdict(list) #uso un default dict per non dover fare il controllo sull'esistenza o no della categoria

    def add_ordine(self, ordine:Ordine):
        #Aggiunge un nuovo ordine agli elemneti da gestire
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        print("\n" + "-"*60)
        print("\n" + "-"*60)
        
        #ASSICURIAMOCI CHE ESISTA L'ORDINE
        if not self._ordini_da_processare:
            print(f"Non ci sono ordini in coda")
            return False

        #Se esiste gestiamo il primo in coda
        ordine = self._ordini_da_processare.popleft() #logica FIFO
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #Aggiornare statistiche su prodotti venduti
        #es:
        #Laptop 10
        #Mouse -5+2

        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.nome]+=riga.quantita

        #Raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente].append(ordine)

        #Archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("Ordine correttamente procesato")
        return True

    def processa_tutti_ordini(self):
        """"Procecca tutti gli ordini presenti in coda"""
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()

        print("Tutti gli ordini sono stati processati")

    def get_statistiche_prodotti(self, top_n:int=5):
        """Questo metodo restituisce info sui prodotti più venduti. qìQuante unità sono state vendute di un certo prodotto"""
        valori=[]
        for prosotto, qunatita in self._statistiche_prodotti.most_common(top_n):
            valori.append(prodotto, qunatita)
        return valori

    def get_distibuzione_categoria(self):
        """Questo emtodo restituisce info su tot fatturato per ogni categoria presente"""
        valori=[]
        for cat in self._ordini_per_categoria.keys():
            ordini=self._ordini_per_categoria[cat]
            totale_Fatturato=sum([o.totale_lordo(0.22) for o in ordini] )
            valori.append((cat, totale_Fatturato))
        return valori

    def stampa_riepiloghi(self):
        """Stampa info di massima"""
        print("\n"+"="*60)
        print(f"Stato attuale del business:")
        print(f"Ordini correttamente gestiti:{len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")

        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print(f"Fatturato per cateogira:")
        for cat, fatturato in self.get_distibuzione_categoria():
            print(f"{cat}: {fatturato}")

def test_modulo():
    sistema=GestoreOrdini()

    ordini=[
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                               RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)
        ], ClienteRecord("Mario Rossi", "mario@gmail.it", "Gold")),
        Ordine([ RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                                 RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
                                 RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                                 RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)
        ], ClienteRecord("Fulvio Binchi", "bianchi@gmail.com","Silver")),

        Ordine([ RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)
        ], ClienteRecord("Giuseppe Averta","giuseppe.averta@gmail.com","Silver")),

        Ordine([ RigaOrdine(ProdottoRecord("Tablet", 900.0), 1), RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)
        ], ClienteRecord("Carlo Masone","carlo@mail.it","Gold")),

        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1), RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)
        ], ClienteRecord("Francesca Pistilli","francesca@gmail.com","Bronze")) ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()
    sistema.stampa_riepiloghi()
            


if __name__ == "__main__":
    test_modulo()














