# Implemente uma função que recebe uma string e remove todos os caracteres duplicados, mantendo a ordem original.
#  Exemplo: print(remover_duplicados("banana")) Saída: "ban" 

def remover_duplicados(texto):
    resultado = ""
    for letra in texto:
        if letra not in resultado:
            resultado += letra
    return resultado

print(remover_duplicados("banana"))