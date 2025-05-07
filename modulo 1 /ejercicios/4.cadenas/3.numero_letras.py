"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
mayúsculas y <n> es el número de letras que tienen el nombre."""

nombre = input("ingrese su nombre: ")
print(f"tu NOMBRE: {nombre.upper()} tiene {len(nombre)} letras") 
#len(): sirve para obtener la longitud de un objeto iterable, como listas, tuplas, cadenas de texto, diccionario y otros tipos de secuencia
