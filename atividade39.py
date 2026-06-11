# Crie uma função que receba um número inteiro e retorne a soma dos seus dígitos. 
# Exemplo: print(soma_digitos(12345)) Saída: 15 

def soma_digitos(n):
    return sum(int(d) for d in str(abs(n)))

print(soma_digitos(12345))