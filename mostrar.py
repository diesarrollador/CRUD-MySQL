import mysql.connector

# creando la coneccion a la base de datos
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clientes"
)


def mostrar():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM datos")
        print("\nToda la información de la tabla datos:\n")
        
        myresult = mycursor.fetchall()
        for i in myresult:
            print("cedula:",i[0], "Nombre:",i[1], "Correo:",i[2], "Provincia:",i[3])
            
    except ImportError():
        print('Ha ocurrido un problema')