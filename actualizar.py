import mysql.connector

# creando la coneccion a la base de datos
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clientes"
)

def actualizar():
    try:
        mycursor = mydb.cursor()
        cedula = input("\nCédula a actualizar: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")
        provincia = input("Ingrese la provincia: ")
        
        sql = "UPDATE datos SET nombre = '{}', correo = '{}', provincia = '{}' WHERE cedula = '{}'".format(nombre, correo, provincia, cedula)
        mycursor.execute(sql)
        mydb.commit()
        #mycursor.close()
        #mydb.close()
        print('\nDatos actualizados correctamente!\n')
        
    except ImportError():
        print('An exception occurred')