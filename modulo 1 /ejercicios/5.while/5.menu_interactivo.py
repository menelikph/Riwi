"""Crea un menú con while que permita al usuario elegir entre opciones (por ejemplo, "1. Saludar", 
"2. Despedirse", "3. Salir") y solo termine cuando elija la opción de salir."""

opcion = 0

def saludo():
    print("hola")

def despedir():
    return "chao"

def menu():
    print("este es el menu: elige una opcion \n1. saludar \n2.despedirse \n3.salir")
    
    while True:
        opcion = input("elige una opcion: 2")
        if opcion == "1":
            saludo()
        elif opcion == "2":
            print(despedir())
        elif opcion == "3":
            print("me sali, chao")
            break
        else:
            print("hey, copie bien el numero")

menu()





