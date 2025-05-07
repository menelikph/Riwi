#Pide al usuario dos números y muestra si el primero NO es igual al segundo (usar operador lógico not combinado con comparación).

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if not (num1 == num2):
    print("El primer numero NO es igual al segundo")
else:
    print("El primer numero es igual al segundo")