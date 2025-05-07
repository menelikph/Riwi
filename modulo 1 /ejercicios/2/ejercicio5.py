#Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces.

palabra =  str(input("Escribe una palabra: "))
num =  int(input("Escribe el numero de veces que quieres que se imprima: "))

for i in range(num):
    print(palabra)