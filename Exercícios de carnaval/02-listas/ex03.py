"""
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser
>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.

"""

#------------------------------------ RESPOSTA

lista = [5, 4, 6, 8, 3, 4]

print(f"O maior elemento é: {max(lista)} e está na posição {lista.index(max(lista))}")
print(f"O menor elemento é: {min(lista)} e está na posição {lista.index(min(lista))}\n")


#------------------------------------ EXPERIMENTANDO

lista = [5, 4, 6, 8, 3, 4]

maior = max(lista)
menor = min(lista)

print(f"O maior elemento é: {maior} e está na posição {lista.index(maior)}")
print(f"O menor elemento é: {menor} e está na posição {lista.index(menor)}\n")


#------------------------------------ EXPERIMENTANDO

lista = [5, 4, 6, 8, 3, 4]

copia_lista = list(lista)
copia_lista.sort()

maior = copia_lista[-1]
menor = copia_lista[0]

print(f"O maior elemento é: {maior} e está na posição {lista.index(maior)}")
print(f"O menor elemento é: {menor} e está na posição {lista.index(menor)}\n")