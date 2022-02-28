"""
------------------------------------ PERGUNTA

Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário

>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

"""

#------------------------------------ RESPOSTA

dic = {"matemática": 81, "física": 83, "química": 87}
# sorted_dic = {}

# lista = list(dic.values())
# lista.sort()



print(sorted(dic.items(), key=lambda x: x[1]))