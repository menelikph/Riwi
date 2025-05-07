#agregar a listas

print("Registros de nombres sin repetir")

nombres = []

print("si desea salir recuerde escribir Salir")
nombre = input("Escribe un nombre: ")

while nombre.lower() != "salir":
    if nombre in nombres:
        print("este nombre ya existe en la lista, porfavor ingresa otro diferente")
    else:
        nombres.append(nombre)

    nombre = input("Escribe otro nombre (o escribe salir para terminar): ")

print("esta es la lista final de los nombres:")
for nombre in nombres:
    print(nombre)

print("Y en la lista se veria reflejado asi:")
print(nombres)