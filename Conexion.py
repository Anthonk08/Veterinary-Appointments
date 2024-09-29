# pip install mysql-connector-python
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
#.env Confidential variables
HOSTNAME = os.getenv("HOSTNAME")
USERLOGIN = os.getenv("USERLOGIN")
PASSWORDLOGIN = os.getenv("PASSWORDLOGIN")
DATABASENAME = os.getenv("DATABASENAME")
PORTNUMBERS = int(os.getenv("PORTNUMBERS"))

class CConexion:
    def ConexionDataBase(self):
        try:
            conexion = mysql.connector.connect(host=HOSTNAME, user=USERLOGIN, password=PASSWORDLOGIN, database=DATABASENAME, port=PORTNUMBERS)
            print("Successfully connected to the database")
            return conexion

        except mysql.connector.Error as error:
            print("Error connecting to database {}".format(error))
            return conexion

app = CConexion()
app.ConexionDataBase()