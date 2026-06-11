#Escreva uma função que verifica se uma sequência de números está ordenada de forma crescente. 
# Exemplo: print(esta_ordenada([1, 2, 3, 4, 5])) Saída: True print(esta_ordenada([5, 3, 2, 1])) Saída: False 

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

print(esta_ordenada([1, 2, 3, 4, 5]))  # Saída: True
print(esta_ordenada([5, 3, 2, 1]))     # Saída: False