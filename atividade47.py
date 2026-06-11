# Implemente uma função que receba uma lista de números e retorne a soma acumulada (lista onde cada elemento é a soma dos elementos anteriores e o atual).
#  Exemplo: print(soma_acumulada([1, 2, 3, 4])) Saída: [1, 3, 6, 10] 

def soma_acumulada(lista):
    resultado = []
    soma = 0
    for num in lista:
        soma += num
        resultado.append(soma)
    return resultado

print(soma_acumulada([1, 2, 3, 4]))