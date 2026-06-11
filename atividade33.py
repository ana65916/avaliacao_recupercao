#  Crie uma função que recebe uma lista de números e retorna a soma dos números que estão em índices pares.
#  Exemplo: print(soma_indices_pares([1, 2, 3, 4, 5, 6])) Saída: 9 

def soma_indices_pares(lista):
    soma = 0
    for i in range(len(lista)):
        if i % 2 == 0:
            soma += lista[i]
    return soma

print(soma_indices_pares([1, 2, 3, 4, 5, 6]))