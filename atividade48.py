#  Crie uma função que calcula o MMC (mínimo múltiplo comum) entre dois números.
#  Exemplo: print(mmc(12, 18)) Saída: 36 

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

print(mmc(12, 18))