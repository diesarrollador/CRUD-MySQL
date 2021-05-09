import mysql.connector

# creando la coneccion a la base de datos
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clientes"
)

def eliminar():
    pass