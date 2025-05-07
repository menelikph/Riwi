#Pide al usuario dos números y muestra la división entera (//) y el módulo (%) entre ellos.
num1 =  int(input("Escribe el primer numero: "))
num2 =  int(input("Escribe el segundo numero: "))

divi = num1 // num2
modulo = num1 % num2

print(f"El resultado de la division es: {divi} y su modulo y/o restante es: {modulo}")