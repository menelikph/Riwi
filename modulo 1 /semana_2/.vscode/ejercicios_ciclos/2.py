#ahora con numeros
suma = 0
mayor = None
menor = None
numeros = []
print("agregar numeros en un array")
print("para salir solo precione 0")
numero = int(input("ingresa el primer numero: "))

while numero != 0:
    if numero in numeros:
        print ("este numero ya esta en la lista")
    else:
        numeros.append(numero)
        suma += numero 
        if mayor is None or numero > mayor:
            mayor = numero
        if menor is None or numero < menor:
            menor = numero
        
    numero = int(input("ingrese otro numero, o preciones 0 para salir: "))
    
print("Esta es la lista de numeros: ")
for numero in numeros:
    print (numero)

print(f"Y el array seria el siguiente {numeros}")
print(f"La suma total es: {suma}")
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
