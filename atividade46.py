# Escreva uma função que retorne a mediana de uma lista de números.
#  Exemplo: print(mediana([1, 2, 3, 4, 5])) Saída: 3 print(mediana([1, 2, 3, 4])) Saída: 2.5 

def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]

print(mediana([1, 2, 3, 4, 5]))  # Saída: 3
print(mediana([1, 2, 3, 4]))     # Saída: 2.5