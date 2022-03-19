"""
------------------------------------ PERGUNTA

Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. 
Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20

"""

#------------------------------------ RESPOSTA

dic = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

nota_max = f"Nota máxima -> {max(dic.items(), key=lambda item: item[1])[0]} : {max(dic.items(), key=lambda item: item[1])[1]}"
nota_min = f"Nota mínima -> {min(dic.items(), key=lambda item: item[1])[0]} : {min(dic.items(), key=lambda item: item[1])[1]}"

print(nota_max)
print(nota_min)