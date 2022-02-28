"""
------------------------------------ PERGUNTA

Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.

"""

#------------------------------------ RESPOSTA

lista = ['1', '7', '99', '15']
lista_convt = []

for n in lista:
    lista_convt.append(int(n))

print(lista_convt)

lista = [1, 7, 99, 15]
lista_convt = []

for n in lista:
    lista_convt.append(str(n))

print(lista_convt)

