#Pide al usuario un número decimal y muestra solo la parte entera de ese número.
import math
num1 = float(input("Escribe un numero decimal: "))

parte_entera = math.floor(num1)
print(f"La parte entera de {num1} es {parte_entera}")

parte_entera = math.modf(num1) 
print(f"La parte entera de {num1} es {parte_entera}")


