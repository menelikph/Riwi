num :int = 1

for i in range(1,21,1):
    if num % 2 == 0:
        print(f"El número es par: {num}")
    else:
        print(f"El número es impar: {num}")
    num += 1