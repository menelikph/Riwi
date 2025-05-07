num_puntos = int(input("ingrese el numero de puntos que quieres ingresar: "))
cuadrantes = []
IC = []
iiC = []
IIIC = []
IVC = []

for i in range(num_puntos):
    print (f"punto numero {i + 1}: ")
    x = int(input("ingresa x: "))
    y = int(input("ingresa y: "))

    if x > 0 and y > 0:
        IC.append(f"({x},{y})")
    elif x < 0 and y > 0:
        iiC.append(f"({x},{y})")
    elif x < 0 and y < y:
        IIIC.append(f"({x},{y})")
    else:
        IVC.append(f"({x},{y})")

print(len(IC))

