from dataclasses import dataclass

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    #FUNZIONE DI HASH UTILE PER I SET
    def __hash__(self):
        return hash((self.name, self.prezzo_unitario))

    def __eq__(self, other):
        self.name==other.name

    def __str__(self):
        return f"{self.name} -- {self.prezzo_unitario}"