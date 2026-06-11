# ) Implemente uma função que encontre a maior sequência de caracteres consecutivos iguais em uma string. 
# Exemplo: print(maior_sequencia("aabbccdddde")) Saída: "dddd" print(maior_sequencia("aaabbbcccc")) Saída: "cccc" 

def maior_sequencia(texto):
    if not texto:
        return ""
    
    max_seq = texto[0]
    atual_seq = texto[0]
    
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            atual_seq += texto[i]
        else:
            if len(atual_seq) > len(max_seq):
                max_seq = atual_seq
            atual_seq = texto[i]
    
    if len(atual_seq) > len(max_seq):
        max_seq = atual_seq
    
    return max_seq

print(maior_sequencia("aabbccdddde"))  # Saída: "dddd"
print(maior_sequencia("aaabbbcccc"))   # Saída: "cccc"