"""
------------------------------------ PERGUNTA

Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após o elemento 6000 na lista acima. 
O resultado final deverá ser:
>>> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


"""

#------------------------------------ RESPOSTA

lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

sublist = lst[2]
sublist.append(7000)

print(lst)