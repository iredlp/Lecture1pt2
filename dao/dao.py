import mysql.connector

from gestionale.core.prodotto import ProdottoRecord
from gestionale.core.cliente import ClienteRecord


#il dao comunica con il db e raccoglie/organizza i suoi dati

class DAO:
    def getAllProdotti(self):
        cnx=mysql.connector.connect(
        user="root",
        password="rootroot",
        host="127.0.0.1",
        database="sw_gestionale",
        )
        cursor=cnx.cursor(dictionary=True)
        cursor.execute("select * from prodotti")
        row=cursor.fetchall() #restituisce tutte le righe pk non abbiamo specificato l'output che mi aspetto

        res = [] #dove salvare i dati raccolti nella query
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="127.0.0.1",
            database="sw_gestionale",
        )
        cursor = cnx.cursor(dictionary=True)
        query = "select * from clienti "
        cursor.execute(query)
        row = cursor.fetchall()  # restituisce tutte le righe pk non abbiamo specificato l'output che mi aspetto

        res = []  # dove salvare i dati raccolti nella query
        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"]))

        cursor.close()
        cnx.close()
        return

    def hasClienti(self, cliente):
        cnx=mysql.connector.connect(
        user="root",
        password="rootroot",
        host="127.0.0.1",
        database="sw_gestionale",
        )
        cursor=cnx.cursor(dictionary=True)
        query="select * from clienti where mail=%s"
        cursor.execute(query, (cliente.mail))
        row=cursor.fetchall() #restituisce tutte le righe pk non abbiamo specificato l'output che mi aspetto
        cursor.close()
        cnx.close()
        return len(row)>0

    def hasProdotto(self, prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="127.0.0.1",
            database="sw_gestionale",
        )
        cursor = cnx.cursor(dictionary=True)
        query = "select * from prodotto where nome=%s"
        cursor.execute(query, (prodotto.nome))
        row = cursor.fetchall()  # restituisce tutte le righe pk non abbiamo specificato l'output che mi aspetto
        cursor.close()
        cnx.close()
        return len(row) > 0

    def addProdotto(self, prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="127.0.0.1",
            database="sw_gestionale",
        )
        cursor = cnx.cursor()
        query="""insert into prodotto(nome, prezzo) values(%s,%s)"""
        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))

        res = []  # dove salvare i dati raccolti nella query

        cnx.commit()
        cursor.close()
        cnx.close()
        return res

    def addClienti(self, cliente):
        cnx = mysql.connector.connect(
            user="root",
            password="rootroot",
            host="127.0.0.1",
            database="sw_gestionale",
        )
        cursor = cnx.cursor()
        query="""insert into clienti(nome,mail, categoria) values(%s,%s,%s)"""

        cursor.execute(query, (cliente.name, cliente.mail, cliente.categoria))

        res = []  # dove salvare i dati raccolti nella query

        cnx.commit()
        cursor.close()
        cnx.close()
        return res


if __name__ == '__main__':
    mydao=DAO()
    mydao.getAllProdotti()