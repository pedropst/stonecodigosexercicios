"""
------------------------------------ PERGUNTA

Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário

>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

"""

#------------------------------------ RESPOSTA

dic = {"matemática": 81, "física": 83, "química": 87}
sorted_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
sorted_dic = dict(sorted_list)

print(sorted_dic)