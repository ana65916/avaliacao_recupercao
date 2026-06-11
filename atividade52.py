# Crie uma função que verifique se uma string é uma anagrama de outra string.
#  Exemplo: print(eh_anagrama("amor", "roma")) Saída: True print(eh_anagrama("python", "java")) Saída: False 


def eh_anagrama(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print(eh_anagrama("amor", "roma"))   
print(eh_anagrama("python", "java")) 