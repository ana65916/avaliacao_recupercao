#Implemente uma função que calcula o número de vogais em uma string.
 #Exemplo: print(contar_vogais("Programação")) Saída: 5 

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais("Programação"))