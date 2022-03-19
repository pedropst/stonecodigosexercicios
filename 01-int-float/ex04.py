"""
------------------------------------ PERGUNTA

Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.

"""

# ------------------------------------ RESPOSTA

peso = float(input("Insira qual é o seu peso em kg: "))
altura = float(input("Insira qual é a sua altura em metros: "))

imc = peso/(altura**2)

print(f"O seu IMC é: {imc:.2f}")


# ------------------------------------ EXPERIMENTANDO
# Para conhecer novas funções do módulo math:

from math import pow

imc = peso/(pow(altura, 2))

print(f"O seu IMC é (calculado com o módulo math): {imc:.2f}")