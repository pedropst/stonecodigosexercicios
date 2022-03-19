"""
------------------------------------ PERGUNTA

Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e imprime-a na tela. 
O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.

"""

# ------------------------------------ RESPOSTA

valores = []
while True:
    valor = float(input('Digite um valor para encontrar a média: '))
    if valor == 0:
        break
    valores.append(valor)

media = sum(valores)/len(valores)
print(media)