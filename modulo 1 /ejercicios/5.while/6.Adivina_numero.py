"""Genera un número secreto (puedes usar una variable fija) 
y usa un while para pedirle al usuario que lo adivine. Da pistas si el número es mayor o menor."""

secret_num = "4"

print("adivina el numero!")

while True:
    option = input("dime un numero: ")
    if option == secret_num:
        print("bien hecho! has adivinado")
        break
    elif option < secret_num:
        print("el numero que ingresaste es MENOR al numero secreto")
    else:
        print("el numero que ingresaste es MAYOR al numero secreto")