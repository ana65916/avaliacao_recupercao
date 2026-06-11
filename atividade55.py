# Escreva uma função que encontre o menor número em uma lista de números. Exemplo: print(menor_numero([3, 5, 7, 2, 8])) Saída: 2 print(menor_numero([10, 20, 30])) Saída: 10 

def menor_numero(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

print(menor_numero([3, 5, 7, 2, 8]))  # Saída: 2
print(menor_numero([10, 20, 30]))     # Saída: 10