# Escreva uma função que calcule a soma dos números ímpares de 1 até um número n dado. Exemplo: print(soma_impares(10)) Saída: 25 

def soma_impares(n):
    soma = 0
    for i in range(1, n + 1, 2):
        soma += i
    return soma

print(soma_impares(10))