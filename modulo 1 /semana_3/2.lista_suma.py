lista = [1,2,3,4,5]
suma:int = 0

for i in lista: #for each: el elemento se guarda en i y se repite hasta que termine la lista
    suma += i

print(suma)

suma = 0

for i in range(len(lista)):
    suma += lista[i]

print(suma)