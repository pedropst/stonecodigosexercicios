"""
------------------------------------ PERGUNTA

Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

"""

# ------------------------------------ RESPOSTA

def reverse(num : int):
    num_str = str(num)
    num_rev = ''
    for d in range(len(num_str) - 1, -1, -1):
        num_rev += num_str[d]
    return int(num_rev)

print(reverse(165115656))