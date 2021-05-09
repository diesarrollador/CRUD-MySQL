import mysql.connector

# creando la coneccion a la base de datos
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clientes"
)

def eliminar():
    try:
        mycursor = mydb.cursor()
        cedula = input("\nIngrese la cédula del cliente a eliminar: ")
        sql = "DELETE FROM datos WHERE cedula = '{}'".format(cedula)
        mycursor.execute(sql)
        mydb.commit()
        print("\nCliente eliminado exitosamente")
        
    except ImportError():
        print('Ha ocurrido un erro')