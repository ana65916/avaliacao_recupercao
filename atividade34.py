 #Escreva uma função que recebe duas listas e retorna uma nova lista que contém apenas os elementos comuns entre elas, sem repetições.
  #Exemplo: print(intersecao_listas([1, 2, 3, 4], [3, 4, 5, 6])) Saída: [3, 4] 

def intersecao_listas(lista1, lista2):
    resultado = []
    for item in lista1:
        if item in lista2 and item not in resultado:
            resultado.append(item)
    return resultado

print(intersecao_listas([1, 2, 3, 4], [3, 4, 5, 6]))