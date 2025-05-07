#Desafío de calificaciones y estadísticas

#1.Determinar el estado de aprobación
#Pedimos una calificacion de 0 a 100 teniendo en cuenta su respectiva validacion
while True:
    nota = int(input("ingresa una calificacion numerica (de 0 a 100): "))
    print("\n") 
    if nota < 0 or nota >100: #se valida que se encuentre en el rango debido
        print("Lo siento, los valores proporcionados no estan en el rango de calificaciones (0 a 100).")
        print("________vuelve a intentarlo________") #si el usuario se equivoca volvemos a preguntar
    elif nota >= 0 or nota <= 100:
        if nota >= 50: # Si la calificación es válida, se evalúa si es mayor o igual a 50
            print("=" * 35)
            print("felicidades, has aprobado")
            print("=" * 35)
        else: # Si la calificación es menor que 50, se muestra que ha reprobado
            print("=" * 35)
            print("=" * 35)
            print("Lo siento, has reprobado")
            print("=" * 35)
        break #se cierra el while
print("\n")

#2. ahora calcular el promedio
lista_calif = []  #Lista donde se almacenarán las calificaciones
suma:int = 0 # Variable para almacenar la suma total de las calificaciones

while True:
    cantidad = int(input("cuantas notas desea colocar?: "))
    print("\n")

    if cantidad <= 0: #se valida segun los datos
        print("\n")
        print("numero icorrecto, vuelve a intentarlo (No numeros negativos o igual a cero)")
        continue # Si la cantidad es inválida, se pide de nuevo la cantidad

    for i in range(cantidad):
        lista_calif.append(int(input(f"ingrese la nota {i + 1}: ")))
        suma += lista_calif[i] # Se suma cada calificación al total
    break # Sale del ciclo una vez que se ingresan todas las calificaciones

promedio = suma / cantidad
print("\n")
print("=" * 45)
print(f"las notas ingresadas son: {lista_calif} \nY el promedio de las calificaciones es: {promedio}")
print("=" * 45)

#3. Contar calificaciones mayores

cal_May = []
print("\n")

while True:
    valor = int(input("ingrese un valor especifico: "))
    print("\n")
    if valor < 0:
        print("invalido, el numero no puede ser nagativo.")
        print("________vuelve a intentarlo________")
        continue
    for i in range(len(lista_calif)):
        if lista_calif[i] > valor :
            cal_May.append(lista_calif[i]) # Se agrega a la lista cal_May si la calificación es mayo
    break #sale del ciclo al completar

if len(cal_May) == 0: # Si la lista de calificaciones mayores está vacía, se informa que no hay resultados
    print("=" * 45)
    print(f"No se encontraron calificaciones mayores a {valor}.")
    print("=" * 45)
else: # Si existen calificaciones mayores, se muestra cuántas hay y cuáles son
    print("=" * 45)
    print (f"los numeros mayores obtenidos por lista son: {cal_May}, lo que en total son {len(cal_May)} calificaciones encontradas que son mayores a {valor}")
    print("=" * 45)
    