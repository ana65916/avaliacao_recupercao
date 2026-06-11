#mplemente uma função que determine se um número é um número perfeito. Um número perfeito é um número que é igual à soma de seus divisores próprios (excluindo ele mesmo).
#Exemplo: print(eh_numero_perfeito(6)) Saída: True print(eh_numero_perfeito(28)) Saída: True print(eh_numero_perfeito(12)) Saída: False 


def eh_numero_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

print(eh_numero_perfeito(6))   # True
print(eh_numero_perfeito(28))  # True
print(eh_numero_perfeito(12))  # False