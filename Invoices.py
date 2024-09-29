from Conexion import *

class CInvoices:
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