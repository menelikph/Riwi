#Pide dos números y muestra si el primero es menor o igual que el segundo (usar operador de comparación).
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if num1 == num2:
    print( "El primer numero es igual al segundo")  
elif num1 < num2: 
    print("El primer numero es menor que el segundo")
else:
    print("no hay concidencias")


