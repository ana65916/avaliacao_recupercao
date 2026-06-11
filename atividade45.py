#  Crie uma função que converta um número romano para um número inteiro. 
# Exemplo: print(romano_para_inteiro("XIV")) Saída: 14 


def romano_para_inteiro(romano):
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    total = 0
    prev = 0
    
    for letra in romano[::-1]:
        valor = valores[letra]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor
    
    return total

print(romano_para_inteiro("XIV"))