#contador de palabras

lista = ["hola", "mundo", "hola", "python"]
contador = {}

for palabra in lista:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1


print(contador)