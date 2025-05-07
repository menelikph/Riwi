#Pide al usuario dos números y muestra si al menos uno es mayor que 10 (usar operador lógico or).
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))

if num1 >= 10 or num2 >= 10:
    print( "uno de los numeros son mayores a 10")  
else:
    print("ninguno es mayor a 10")