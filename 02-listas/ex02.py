"""
------------------------------------ PERGUNTA

Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a lista na ordem inversa. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] a saída deve ser
>>> [[7,7,7], “H”, 6, 3, 1]

"""

#------------------------------------ RESPOSTA

from re import I


lista = [0, 1.0, 10, False, "quatro", "V", 6, set(["e", "e", "e"]), 'oito', 9]
lista.reverse()

print(lista)


#------------------------------------ EXPERIMENTANDO

lista = [0, 1.0, 10, False, "quatro", "V", 6, set(["e", "e", "e"]), 'oito', 9]
lista_reversa = []
for i in range(len(lista) - 1, -1, -1):
    lista_reversa.append(lista[i])

print(lista_reversa)