"""
------------------------------------ PERGUNTA

Embaralha palavras: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

"""

#------------------------------------ RESPOSTA
from random import randint

def embaralhar(palavra : str):
    random_list = []
    embaralhada = ''
    while True:
        r = randint(0, len(palavra) - 1)
        if r not in random_list:
            random_list.append(r)
            embaralhada += palavra[r]
        elif len(embaralhada) == len(palavra):
            break

    return embaralhada.upper()

print(embaralhar('python'))