saldo:float = 1200
deposito:float = 0
retirar:float = 0
opcion:int 

print("Bienvenido al cajero automatico")


while True:
    print("escoje una opcion: ")
    print("presione 1 para ver saldo ")
    print("presione 2 para depositar dinero ")
    print("presione 3 para retirar dinero ")
    opcion = int(input(":"))

    if opcion == 1:
        print(f"Tu saldo actual es: {saldo}")
        break

    elif opcion == 2:
        print("depositar dinero \ncuanto desea depositar: ")
        deposito = int(input ())
        if deposito <= 0:
            print(f"Lo siento pero el saldo es insuficiente, en tu cuenta hay ${saldo}")
        else:
            print(f"has depositado {deposito} y en tu cuenta queda ${saldo + deposito} de saldo")
        break

    elif opcion == 3:
        print("retiro de dinero \ncuanto desea retirar?: ")
        retirar = int(input ())
        if retirar <= saldo:
            print(f"has retirado {retirar} y en tu cuenta queda ${saldo - retirar} de saldo")
        else:
            print(f"Lo siento pero el saldo es insuficiente, en tu cuenta hay ${saldo}")
        break 
    else:
        print(f"lo siento pero la opcion no es validad, vuelva a intentarlo")