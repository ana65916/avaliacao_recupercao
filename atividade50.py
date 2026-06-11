#  Implemente uma função que calcula o produto de dois números inteiros sem utilizar o operador de multiplicação (*).
# Utilize apenas adições e subtrações. Exemplo: print(multiplicacao(6, 7))
#  Saída: 42 print(multiplicacao(-6, 7)) Saída: -42 print(multiplicacao(6, -7)) 
# Saída: -42 print(multiplicacao(-6, -7)) Saída: 42 

def multiplicacao(a, b):
    resultado = 0
    negativo = (a < 0) ^ (b < 0)  # XOR: True se apenas um dos números é negativo
    a, b = abs(a), abs(b)
    
    for _ in range(b):
        resultado += a
    
    if negativo:
        resultado = -resultado
    
    return resultado

print(multiplicacao(6, 7))     # Saída: 42
print(multiplicacao(-6, 7))    # Saída: -42
print(multiplicacao(6, -7))    # Saída: -42
print(multiplicacao(-6, -7))   # Saída: 42