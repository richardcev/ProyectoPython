import funciones
def menu():
    opcion='inicio'
    opcion_salida = '0'
    while opcion != opcion_salida:
        print("**************************")
        print("1. LEER EL ARCHIVO TXT")
        print("2. CALCULAR Y MOSTRAR LOS SALARIOS")
        print("3. MOSTRAR RUTA DEL ARCHIVO TXT")
        print("4. CAMBIAR RUTA DEL ARCHIVO TXT")
        print("0. SALIR")
        print("**************************")
        opcion = input("Ingresa una opción(0-4): ")
        ejecutarOpcion(opcion)


def ejecutarOpcion(numOpcion):
    if numOpcion=='1':
        print(funciones.leerArchivoTxt())
    elif numOpcion=='2':
        funciones.llenarListas()


#Ejecicion del programa
menu()





