"""
------------------------------------ PERGUNTA

Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. 
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.

"""

# ------------------------------------ RESPOSTA
# talvez a maneira mais simples de resolver, receber do input uma string, uma variável para cada dígito, transformar em int cada variável e somar

numero = input("Digite um número de 4 dígitos: ")
n1 = int(numero[0])
n2 = int(numero[1])
n3 = int(numero[2])
n4 = int(numero[3])

print(f"A soma dos dígitos é: {n1+n2+n3+n4}")


# ------------------------------------ EXPERIMENTANDO
# receber o input como um número, utilizar conceito de milhar, centena, dezena e unidade para separar cada dígito e somá-los ao final

numero = int(input("Digite um número de 4 dígitos: "))

unidade_de_milhar = numero//1000
numero = numero - unidade_de_milhar*1000

centena = numero//100
numero = numero - centena*100

dezena = numero//10
numero = numero - dezena*10

unidade = numero

print(f"A soma dos dígitos é: {unidade_de_milhar + centena + dezena + unidade}")


# ------------------------------------ EXPERIMENTANDO
# Quando não houver a quantidade definida de dígitos:

numero = input("Digite um número: ")

soma = 0
for char in numero:
    soma += int(char)

print(f"A soma dos dígitos é: {soma}")