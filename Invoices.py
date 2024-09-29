from Conexion import *

class CInvoices:
    def showInvoice():
        try:
            conexion = CConexion()
            cone = conexion.ConexionDataBase()
            cursor = cone.cursor()
            cursor.execute("select * from invoices;")
            # Show all the table information
            myResult = cursor.fetchall()
            cone.commit()
            cone.close()

            return myResult

        except mysql.connector.Error as error:
            print("Error shows dates {}".format(error))

    def enterInvoice(client, phone, email, service, petName, petSex):
        try:
            conexion = CConexion()
            cone = conexion.ConexionDataBase()
            cursor = cone.cursor()
            sql = "insert into invoices values(null, %s, %s, %s, %s, %s, %s);"
            # Values variable is a tupla
            values = (client, phone, email, service, petName, petSex)
            cursor.execute(sql, values)
            cone.commit()
            print(cursor.rowcount,"Registration entered successfully")
            cone.close()

        except mysql.connector.Error as error:
            print("Error enter dates {}".format(error))