#  Implemente uma função que inverte as palavras de uma string mantendo a ordem das palavras.
#  Exemplo: print(inverter_palavras("Olá mundo")) Saída: "ola mundo " 

def inverter_palavras(frase):
    palavras = frase.split()
    invertidas = []

    for p in palavras:
        invertidas.append(p[::-1])

    return " ".join(invertidas)

print(inverter_palavras("Olá mundo"))