import insertar, mostrar, actualizar, eliminar

class Principal():
    def __init__(self):
        self.bandera = 1
        
    def menu(self):
        while self.bandera:
            select = input(""" \n1 insertar\n2 mostrar\n3 actualizar\n4 eliminar\n5 salir
                        \ningrese su elección:  """)
            if select == '1':
                insertar.insertar()
            elif select == '2':
                mostrar.mostrar()
            elif select == '3':
                mostrar.mostrar()
                actualizar.actualizar()
            elif select == '4':
                mostrar.mostrar()
                eliminar.eliminar()
            elif select == '5':
                break
            else :
                print("Número incorrecto.")

obj1 = Principal()
obj1.menu()