baceD = 3080
nombre = "menelik"
contra = "123ph"

print("bienvenido al puerto N 3080")

while True:
    usuario = input("ingrese su usuiario: ")
    if usuario == nombre:
        print(f"El usuario {usuario} fue encontrado en la base de datos")
        break
    elif not (usuario == nombre):
        print(f"El usuario {usuario} NO fue encontrado en la base de datos")
        print("intentelo de nuevo")

intentos = 0
max_inten = 4

while intentos < max_inten:
    con = input("ingrese su contraseña: ")
    if contra == con:
        print(f"la contraseña es correcta")
        print("has ingresado correctamente")
    else:
        intentos +=1
        print(f"la contraseña es incorrecta, numero de intento {intentos} de {max_inten}")
        if intentos == max_inten:
          print("Has alcanzado el número máximo de intentos. Acceso bloqueado.")
          break
        else:
            print("intentelo de nuevo")
    

    

