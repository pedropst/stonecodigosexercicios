"""
------------------------------------ PERGUNTA

Um determinado zoológico cobra a entrada com base na idade do visitante. 
Os visitantes com 2 anos de idade ou menos não pagam para entrar. 
Crianças entre 3 e 12 anos custa R$14,00. Idosos com 65 anos ou mais custam R$18,00. 
A entrada para todos os outros visitantes é de R$23,00. 
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha. 
O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo. 
Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada. 
O custo deve ser exibido usando duas casas decimais.

"""

# ------------------------------------ RESPOSTA

idades = []
while True:
    idade = input('Qual é a idade do visitante: ')
    if idade == '':
        break
    idades.append(idade)

preco_total = 0
for idade in idades:
    if int(idade) <= 2:
        continue
    elif int(idade) >= 3 and int(idade) <= 12:
        preco_total += 14
    elif int(idade) >= 65:
        preco_total += 18
    else:
        preco_total += 23
print(preco_total)