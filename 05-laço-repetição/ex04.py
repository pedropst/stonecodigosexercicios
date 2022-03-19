"""
------------------------------------ PERGUNTA

Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita)
Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!

"""

# ------------------------------------ RESPOSTA

pi = 3
aproximacoes = 15
for n in range(2, aproximacoes*2-3, 4):
    pi += 4/(n*(n+1)*(n+2)) - 4/((n+2)*(n+3)*(n+4))

print(pi)