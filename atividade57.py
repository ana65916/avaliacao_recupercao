# Crie uma função que verifique se uma lista está ordenada em ordem crescente.
#  Exemplo: print(esta_ordenada([1, 2, 3, 4, 5])) Saída: True print(esta_ordenada([1, 3, 2, 4])) Saída: False 

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

print(esta_ordenada([1, 2, 3, 4, 5]))  # Saída: True
print(esta_ordenada([1, 3, 2, 4]))     # Saída: False