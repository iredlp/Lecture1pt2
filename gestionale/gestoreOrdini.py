"""
Scrivere un software gestionale che abbia le seguenti funzionalità:
1) supportare l'arrivo e la gestione di ordini.
1bis) quando arriva un nuovo ordine, lo aggiungo ad una coda,
assicurandomi che sia eseguito solo dopo gli altri.
2) avere delle funzionalità per avere statistiche sugli ordini
3) fornire statistiche sulla distribuzione di ordini per categoria di cliente.
"""
from collections import deque, Counter, defaultdict
from random import random

from dao.dao import DAO
from gestionale.core.prodotto import ProdottoRecord
from gestionale.gestoreOrdiniMio import ClienteRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)
        self._dao = DAO()  # ISTANZA DEL DAO PER POTER USARE I METODI
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self):
    #leggo prodotti e cienti dal DB e poi creo degli orsini randomici per testare l'app
        self._allP.extend(self._dao.getAllProdotti())
        self._allC.extend(self._dao.getAllClienti())

        for i in range(10):
            indexP= random.randint(0,len(self._allP)-1)
            indexC = random.randint(0, len(self._allC)-1)

            ordine=Ordine([RigaOrdine(self._allP[indexP], random.radint(1,5))],
                          self._allC[indexC])
            self.add_ordine(ordine)

    def add_ordine(self, ordine: Ordine):
        """Aggiunge un nuovo ordine agli elementi da gestire"""
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}.")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def crea_ordine (self, nomeP, prezzoP, quantitaP,
                     nomeC, mailC, categoriaC):
        return Ordine([RigaOrdine(ProdottoRecord(nomeP, prezzoP), quantitaP)],
                      ClienteRecord(nomeC, mailC, categoriaC))

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        print("\n" + "-"*60)
        print("\n" + "-"*60)

        #Assicuriamoci che un ordine da processare esista.
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda.")
            return False, Ordine([], ClienteRecord("", "", " "))

        #Se esiste, gestiamo il primo in coda.
        ordine = self._ordini_da_processare.popleft() # Loigica FIFO

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #Aggiornare statistiche sui prodotti venduti --
        # Laptop - 10 +1
        # Mouse - 5 +2
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        #Raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #Archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato.")

        return True, ordine

    def processa_tutti_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda."""
        print("\n" + "="*60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini sono stati processati.")

    def get_statistiche_prodotti(self, top_n: int = 5):
        "Questo metodo restituisce info sui prodotti più venduti. "
        valori = []
        for prodotto, quantità in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantità))
        return valori

    def get_distribuzione_categorie(self):
        """Questo metodo restituisce info su totale fatturato per ogni categoria presente"""
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_Fatturato = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat, totale_Fatturato))
        return valori

    def get_riepilogo(self):
        """Restituisce una stringa con le info di massiam"""
        sommario=" "
        sommario+=("\n" + "="*60)
       # sommario +=("Stato attuale del business:")
        sommario +=(f"\nOrdini correttamente gestiti: {len(self._ordini_processati)}")
        sommario +=(f"\nOrdini in coda: {len(self._ordini_da_processare)}")

        sommario +=("\nProdotti più venduti:")
        for prod, quantità in self.get_statistiche_prodotti():
            sommario +=(f"\n{prod}: {quantità}")

        sommario +=(f"\nFatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario +=(f"\n{cat} : {fatturato}")
        return sommario
        sommario += ("\n" + "=" * 60)

def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Mario Rossi", "mario@mail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
               ClienteRecord("Fulvio Bianchi", "bianchi@gmail.com", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)],
            ClienteRecord("Giuseppe Averta", "giuseppe.averta@polito.it", "Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 900.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
            ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
            ClienteRecord("Francesca Pistilli", "francesca@gmail.com", "Bronze"))
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()

    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()










