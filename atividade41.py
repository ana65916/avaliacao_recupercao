# Implemente uma função que conte quantas vezes cada caractere aparece em uma string.
#  Exemplo: print(contar_caracteres("abacaxi")) Saída: {'a': 3, 'b': 1, 'c': 1, 'x': 1, 'i': 1} 


def contar_caracteres(texto):
    contagem = {}
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

print(contar_caracteres("abacaxi"))