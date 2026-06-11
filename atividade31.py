# Implemente uma função que recebe uma lista de números e retorna uma
#  nova lista contendo apenas os números pares. Exemplo: print(filtrar_pares([1, 2, 3, 4, 5, 6])) Saída: [2, 4, 6] 

def filtrar_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

print(filtrar_pares([1, 2, 3, 4, 5, 6]))