import math

def hi(name:str="deconocido"):
    
    print("hi " + name)

def suma(a:int,b:int)-> int:
   
   result = a + b
   return result

def area_circulo(r):
   area = math.pi * r**2
   return area

def es_par(numero):
   if numero % 2 == 0:
       return True
   else:
       return False

def mayor_de_tres(a,b,c):
   if a > b and a > c:
      return a
   elif b > a and b > c:
      return b
   else:
      return c
      
def contar_vocales(word):
   vocal = 0
   word = word.lower()
   for i in range(len(word)):
      if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
         vocal += 1
   return vocal

def main():
   hi("mene")

   result = suma(5,5)
   print(result)
   
   print(area_circulo(12))

   print(es_par(4))

   print(mayor_de_tres(20, 12, 4))

   print(contar_vocales("pErro"))



main()