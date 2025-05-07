# Programa de calificaciones 

# 1. Estado de aprobación
nota = int(input("ingresa una calificacion numerica (de 0 a 100): "))

#se valida que se encuentre en el rango debido
if nota < 0 or nota >100:
    print("Lo siento, los valores proporcionados no estan en el rango de calificaciones (0 a 100). Vuelva a intentarlo")
elif nota >= 0 or nota <= 100:
    if nota >= 50:
        print("felicidades, has aprovado")
    else:
        print("Lo siento, has reprovado")


# 2. Calcular promedio
cantidad = int(input("¿Cuántas calificaciones quiere ingresar? "))
suma = 0
contador = 0

while contador < cantidad:
    nota = int(input(f"Ingrese la calificación {contador + 1}: "))
    suma += nota
    contador += 1

promedio = suma / cantidad
print("Promedio:", promedio)

print("---")

# 3. Contar calificaciones mayores
valor = int(input("Ingrese un valor para comparar: "))
contador_mayores = 0
contador = 0

while contador < cantidad:
    nota = int(input(f"Ingrese nuevamente la calificación {contador + 1}: "))
    if nota > valor:
        contador_mayores += 1
    contador += 1

print(f"Calificaciones mayores que {valor}: {contador_mayores}")

print("---")

# 4. Verificar y contar una calificación específica
buscar = int(input("Ingrese la calificación que desea contar: "))
contador_buscar = 0
contador = 0

while contador < cantidad:
    nota = int(input(f"Ingrese nuevamente la calificación {contador + 1}: "))
    if nota == buscar:
        contador_buscar += 1
    contador += 1

print(f"La calificación {buscar} aparece {contador_buscar} veces.")
