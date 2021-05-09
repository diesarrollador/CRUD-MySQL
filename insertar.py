import mysql.connector

# creando la coneccion a la base de datos
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clientes"
)

# gestiona las operaciones de la base de datos 

def insertar():
    try:
        mycursor = mydb.cursor()
        cedula_cliente = input("Ingrese la cédula: ")
        nombre_cliente = input("Ingrese el nombre: ")
        correo_cliente = input("Ingrese el correo: ")
        provincia_cliente = input("Ingrese la provincia: ")
        
        sql = """ INSERT INTO datos (cedula, nombre, correo, provincia) 
        VALUES('{}', '{}', '{}', '{}') """.format(cedula_cliente, nombre_cliente, correo_cliente, provincia_cliente)
        mycursor.execute(sql)
        mydb.commit()
        #mycursor.close()
        #mydb.close()
        print('\nDatos insertados correctamente!\n')
        
    except ImportError():
        print("Algo ha ido mal")