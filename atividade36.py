# Crie uma função que receba uma lista de números e retorne o segundo maior número.
#  Exemplo: print(segundo_maior([10, 20, 4, 45, 99, 99])) Saída: 45 

def segundo_maior(lista):
    unicos = list(set(lista))
    unicos.sort()
    return unicos[-2]

print(segundo_maior([10, 20, 4, 45, 99, 99]))