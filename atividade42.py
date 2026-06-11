# Crie uma função que receba uma lista de strings e retorne a mais longa.
#  Exemplo: print(string_mais_longa(["casa", "carro", "avião"])) Saída: "carro" 

def string_mais_longa(lista):
    maior = lista[0]
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    return maior

print(string_mais_longa(["casa", "carro", "avião"]))