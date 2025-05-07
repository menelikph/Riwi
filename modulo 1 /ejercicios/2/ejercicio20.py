#Pide al usuario un número entero y muestra si el número es divisible entre 5 (usar operador de módulo % y comparación).
num1 = int(input("Escribe un numero: "))

if num1 % 5 == 0:
    print("El numero es divisible entre 5")
else:
    print("El numero NO es divisible entre 5")