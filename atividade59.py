# Implemente uma função que calcule a soma dos quadrados dos números em uma lista. 
# Exemplo: print(soma_quadrados([1, 2, 3])) Saída: 14 print(soma_quadrados([4, 5, 6])) Saída: 77 

def soma_quadrados(lista):
    soma = 0
    for num in lista:
        soma += num ** 2
    return soma

print(soma_quadrados([1, 2, 3]))  # Saída: 14
print(soma_quadrados([4, 5, 6]))  # Saída: 77