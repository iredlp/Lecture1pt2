import pathlib

import mysql

@classmethod #così non crea un istanza ogni volta richiamo, diventa un metodo della classe.
class dbConnect:
    _mypool=None

    def __init__(self):
        #impedisce al chimante di modifc l'istanza E PER IMPLEMENTARE IL PATTENR SINGLETONE
        raise RuntimeError("Attenzione! Non devi creare un'istanza di questa classe. Usa i metodi di classe")

    @classmethod
    def getConnection(cls):
        if cls._mypool is None:
            try: #UNA CONNESSIONE
                #cnx=mysql.connector.connect(
                  #  user="root",
                   # password="rootroot",
                   # host="127.0.0.1",
                   # database="sw_gestonale"
                #)

                #CRE UN POOL DI CONNESSIONI
                cls.myPool=mysql.connector.pooling.MySQLConnectionPool()
                #user = "root",
                #password="rootroot",
                #host="127.0.0.1",
                #database = "sw_gestonale",
                option_files= f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"

                pool_size=3,
                pool_name="myPool"
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al  database")
                print(err)
                return None
        else:
            #allora la connessione già esiste, quindi la returno
             return cls._myPool.get_connection()