import mysql


class dbConnect:
    def getConnection(self):
        try:
            cnx=mysql.connector.connect(
                user="root",
                password="rootroot",
                host="127.0.0.1",
                database="sw_gestonale"
            )
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al  database")
            print(err)
            return None