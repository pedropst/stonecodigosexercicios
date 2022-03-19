"""
------------------------------------ PERGUNTA

Escreva um programa que diga se um número dado pelo usuário é par ou ímpar

"""

#------------------------------------ RESPOSTA

number = int(input('Digite um número: '))

if number%2 == 0:
    print('O número é par!')
else:
    print('O número é impar!')

#------------------------------------ EXPERIMENTANDO

number = int(input('Digite um número: '))

if number&1 == 0:
    print('O número é par!')
else:
    print('O número é impar!')