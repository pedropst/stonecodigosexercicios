"""
------------------------------------ PERGUNTA

A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns

Barulho	            Nível sonoro (dB)
Britadeira	            130
Cortador de grama	    106
Despertador	            70
Cômodo em silêncio	    40

Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. 
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 

"""

#------------------------------------ RESPOSTA

niveis = {'britadeira' : 130, 'cortador de grama' : 106, 'despertador' : 70, 'cômodo em silêncio' : 40}

nivel_inserido = int(input("Digite o nível em (dB): "))

niveis_list = list(niveis.items())

for item in niveis_list:
    if nivel_inserido == item[1]:
        print(f'O nível inserido equivale foi {nivel_inserido} equivalente à {item[0]}.')
else:
    sorted_dic = sorted_list = sorted(niveis.items(), key=lambda x: x[1], reverse=True)
    sorted_dic = dict(sorted_list)

    sorted_level_list = list(sorted_dic.items())

    for i in range(len(sorted_level_list)):
        if (i + 1 <= len(sorted_level_list)) and (nivel_inserido < sorted_level_list[i][1] and nivel_inserido > sorted_level_list[i+1][1]):
            print(f'O nível inserido equivale foi {nivel_inserido} está entre {sorted_level_list[i][0]} e {sorted_level_list[i+1][0]}') 

