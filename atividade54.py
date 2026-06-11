#Crie uma função que gere o fatorial de um número inteiro n usando apenas um loop for.
#  Exemplo: print(fatorial(5)) Saída: 120 print(fatorial(0)) Saída: 1 

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial(5))  # Saída: 120
print(fatorial(0))  # Saída: 1