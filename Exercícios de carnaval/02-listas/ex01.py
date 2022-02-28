"""
------------------------------------ PERGUNTA

Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). 
Imprima na tela o elemento e sua respectiva posição na lista. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:
>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3

"""

#------------------------------------ RESPOSTA

lista = [151, "string", 51.2, True, {"oi": ",", "como": "você", "está": "?"}]
print(f"""Elemento {lista[0]} na posição {lista.index(lista[0])},
Elemento {lista[1]} na posição {lista.index(lista[1])},
Elemento {lista[2]} na posição {lista.index(lista[2])},
Elemento {lista[3]} na posição {lista.index(lista[3])},
Elemento {lista[4]} na posição {lista.index(lista[4])}.\n""")


#------------------------------------ EXPERIMENTANDO 1

for elemento in lista:
    print(f"Elemento {elemento} na posição {lista.index(elemento)}")


#------------------------------------ EXPERIMENTANDO 2

print("")
for i in range(0, len(lista)):
    print(f"Elemento {lista[i]} na posição {i}")
