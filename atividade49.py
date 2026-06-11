# Crie uma função que determine se dois números são amigos. Dois números são considerados amigos se a soma dos divisores próprios de um número é igual ao outro número e vice-versa. Exemplo: print(sao_amigos(220, 284))
#  Saída: True print(sao_amigos(1184, 1210)) Saída: True print(sao_amigos(30, 42)) Saída: False 

def soma_divisores_proprios(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

def sao_amigos(a, b):
    return soma_divisores_proprios(a) == b and soma_divisores_proprios(b) == a

print(sao_amigos(220, 284))   # Saída: True
print(sao_amigos(1184, 1210)) # Saída: True
print(sao_amigos(30, 42))     # Saída: False