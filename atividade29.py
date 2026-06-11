#Criar uma função que verifica se um número é par. 

def eh_par(numero):
    return numero % 2 == 0

n = int(input("Digite um número: "))

if eh_par(n):
    print("O número é par.")
else:
    print("O número é ímpar.")