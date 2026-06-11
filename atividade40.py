#  Escreva uma função que gere todos os números primos até um dado número n. 
# def gerar_primos(n): Exemplo: print(gerar_primos(20)) Saída: [2, 3, 5, 7, 11, 13, 17, 19] 


def gerar_primos(n):
    primos = []
    for num in range(2, n + 1):
        é_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                é_primo = False
                break
        if é_primo:
            primos.append(num)
    return primos

print(gerar_primos(20))