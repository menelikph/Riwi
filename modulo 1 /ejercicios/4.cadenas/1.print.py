"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas 
distintas el nombre del usuario tantas veces como el número introducido."""
# Solicitar el nombre del usuario
nombre = input("Introduce tu nombre: ")
num = int(input("introduce un numero: "))

print(f"{nombre} \n" * num)