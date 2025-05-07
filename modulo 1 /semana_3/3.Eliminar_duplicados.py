#eliminar duplicados de una lista 

lista = [1,2,2,3,4,4,5]

def eliminar_duplicados(lista):
    no_duplicados = []
    for i in lista:
        if i not in no_duplicados:
            no_duplicados.append(i)
    return no_duplicados
        

print(eliminar_duplicados(lista))

lista2 = [1,1,1,1,3,3,3,5,6,3,3,3,8,8]

def eliminar_duplicados2(lista2):
    lista_no_duplicada = []
    for e in lista2:
        if e not in lista_no_duplicada:
            lista_no_duplicada.append(e)
    return lista_no_duplicada

print(eliminar_duplicados2(lista2))