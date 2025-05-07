print("dame tus tres notas")
nota1:float = input()
nota2:float = input()
nota3:float = input()
promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 and promedio < 7:
    print("Regular")
else:
    print("Reprobado")  