#Pide al usuario dos números y muestra la suma, resta, multiplicación y división (separadas por coma).
num1 =  int(input("Escribe el primer numero: "))
num2 =  int(input("Escribe el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2

print("Los resultados son: ")
print(f"Suma: {suma},  Resta: {resta}, Multiplicación: {multi}, División: {divi}")