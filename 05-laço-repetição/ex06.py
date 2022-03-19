"""
------------------------------------ PERGUNTA

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.

"""

# ------------------------------------ RESPOSTA

h = 0

for n in range(1, int(input('Qual é a quantidade de termos? '))):
    h += 1/n

print(h)