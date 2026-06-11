 #Crie uma função que receba uma lista e uma posição, e retorne o elemento na posição indicada, mas com todos os elementos após essa posição removidos.
  #Exemplo: print(cortar_lista([1, 2, 3, 4, 5], 2)) Saída: [1, 2, 3] print(cortar_lista([10, 20, 30, 40], 1)) Saída: [10, 20]  




def cortar_lista(lista, posicao):
    # Adiciona 1 à posição para incluir o elemento indicado
    return lista[:posicao + 1]

print(cortar_lista([1, 2, 3, 4, 5], 2))  # Saída: [1, 2, 3]
print(cortar_lista([10, 20, 30, 40], 1)) # Saída: [10, 20]