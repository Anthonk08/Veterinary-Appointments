from Conexion import *

class CInvoices:
    #Show dates
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

    #Enter dates
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

    #Update dates
    #update invoices set invoices.cliente = '', invoices.phone = '', invoices.email = '', invoices.service = '', invoices.petName = '', invoices.petSex = '' where invoices.id = 2;
    def modifyData(idInvoices, client, phone, email, service, petName, petSex):
        try:
            conexion = CConexion()
            cone = conexion.ConexionDataBase()
            cursor = cone.cursor()
            sql = "update invoices set invoices.client = %s, invoices.phone = %s, invoices.email = %s, invoices.service = %s, invoices.petName = %s, invoices.petSex = %s where invoices.id = %s;"
            # Values variable is a tupla
            values = (client, phone, email, service, petName, petSex, idInvoices)
            cursor.execute(sql, values)
            cone.commit()
            print(cursor.rowcount,"Registration updated successfully")
            cone.close()

        except mysql.connector.Error as error:
            print("Error updates dates {}".format(error))

    #Eliminate Date
    def eliminateData(idInvoices):
        try:
            conexion = CConexion()
            cone = conexion.ConexionDataBase()
            cursor = cone.cursor()
            sql = "delete from invoices where invoices.id = %s;"
            # Values variable is a tupla
            values = (idInvoices,)
            cursor.execute(sql, values)
            cone.commit()
            print(cursor.rowcount,"Registration eliminated successfully")
            cone.close()

        except mysql.connector.Error as error:
            print("Error eliminate date {}".format(error))