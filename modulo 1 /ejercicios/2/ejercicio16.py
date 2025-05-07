#Pide al usuario dos números y muestra si ambos son mayores que 10 (usar operador lógico and).

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if num1 >= 10 and num2 >= 10:
    print( "los numeros son mayores a 10")  
else:
    print("uno de los numeros es menor a 10")