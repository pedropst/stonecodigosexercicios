"""
------------------------------------ PERGUNTA

Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.

"""

#------------------------------------ RESPOSTA

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

if n1%n2 == 0:
    print(f'{n1} é divisível por {n2}')
else: 
    print(f'{n1} não é divisível por {n2}')