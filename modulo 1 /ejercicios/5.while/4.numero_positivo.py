num = int(input("quieres entrar al ciclo (pon un numero negativo) sino pon un numero positivo: "))

if num > 0:
    print("no has entrado al ciclo")

while num < 0:
    num = int(input("quieres seguir (pon un numero negativo) sino pon un numero positivo: "))
    if num < 0:
        print("sigue el ciclo")
    else:
        print("el ciclo termina")
        break
    