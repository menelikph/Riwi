#Pide un número entero y muestra el número elevado a la 2 (al cuadrado) y a la 3 (al cubo), usando f-strings.
num1 =  int(input("Escribe un numero: "))

cuadrado = num1 ** 2
cubo = num1 ** 3

print(f"El cuadrado de {num1} es {cuadrado} y el cubo es {cubo}.")