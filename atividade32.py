# Escreva uma função que verifica se uma string é um palíndromo 
# (lê-se da mesma forma de trás para frente). Exemplo: print(eh_palindromo("A base do teto desaba")) Saída: True 


def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

print(eh_palindromo("A base do teto desaba"))