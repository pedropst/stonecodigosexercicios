"""
------------------------------------ PERGUNTA

Faça um programa que remova strings vazias de uma lista de strings. 
Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]

"""

#------------------------------------ RESPOSTA

lista = ['Olá', '', 'meu', 'nome', '', 'é', 'facilitador', '']

while '' in lista:
    lista.remove('')

print(lista)