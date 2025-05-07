#Pide al usuario su edad y muestra un mensaje que diga si su edad es mayor que 18 (usar operadores de comparación, sin condicionales).
edad = int(input("Cual es tu edad?: "))

if edad >= 18:
    print("tu eres mayor de edad")
else:
    print("eres menor")

#_________________________________________________________
#Pide al usuario su edad y muestra un mensaje que diga si su edad es mayor que 18 (usar operadores de comparación, sin condicionales).
edad = int(input("Cual es tu edad?: "))

print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")