#invertir una lista

lista = [40,30,20,10]
reverso = []

for i in range(len(lista)-1, -1, -1):
    reverso.append(lista[i])

print(lista)
print(reverso)


"""
#este si se utilisa  slicing
lista = [40, 30, 20, 10]
reverso = lista[::-1]
print(reverso)
"""

