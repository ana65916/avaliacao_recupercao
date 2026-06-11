# Escreva uma função que encontre todos os números primos até um número n sem utilizar a biblioteca math.
#  Exemplo: print(primos_ate_n(20)) Saída: [2, 3, 5, 7, 11, 13, 17, 19] 

def primos_ate_n(n):
    primos = []
    
    for num in range(2, n + 1):
        eh_primo = True
        
        for i in range(2, num):
            if num % i == 0:
                eh_primo = False
                break
        
        if eh_primo:
            primos.append(num)
    
    return primos

print(primos_ate_n(20))