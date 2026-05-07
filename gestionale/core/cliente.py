from dataclasses import dataclass

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    def __hash__(self):
        return hash(self.mail) #DELEGATION: per dire che 2 oggetti sono uguali sulla base della chiave primaria

    def __eq__(self, other):
        self.mail == other.mail #confrontato con la chiave primaria

    def __str__(self):
        return f"{self.nome}-- {self.mail}({self.categoria})" #RAPP  a stringa dell'oggetto
    