#Pide dos números y muestra si el primero es mayor que el segundo (usar operador de comparación).
num1 =  int(input("Escribe el primer numero: "))
num2 =  int(input("Escribe el segundo numero: "))

if num1 > num2:
    print("el primer numero es mayor que el segundo")
else:
    print("El primer numero no es mayor que el segundo")


#Pide dos números y muestra si el primero es mayor que el segundo (usar operador de comparación).
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

print("El primer numero es mayor que el segundo" if num1 > num2 else "El primer numero no es mayor que el segundo")