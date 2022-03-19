"""
------------------------------------ PERGUNTA

Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}

"""

#------------------------------------ RESPOSTA

dic = {1: "vermelho", 2: "azul", 3: "marrom"}
new_dic = {}

for key in dic.keys():
    new_dic[key] = len(dic[key])

print(new_dic)

