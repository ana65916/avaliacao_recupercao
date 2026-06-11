#  Solicitar ao usuário para digitar um número e verificar se ele é positivo


num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")