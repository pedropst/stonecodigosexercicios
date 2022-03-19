"""
------------------------------------ PERGUNTA

Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, 
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informadas ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

"""

# ------------------------------------ RESPOSTA

nome = input("Qual é o nome do(a) atleta? ")
notas = []

for _ in range(7):
    notas.append(float(input("Digite uma nota: ")))

nota_max = max(notas)
nota_min = min(notas)

notas.remove(nota_max)
notas.remove(nota_min)

media = sum(notas)/len(notas)

print(f"""\nResultado final:
Atleta: {nome}
Melhor nota: {nota_max}
Pior nota: {nota_min}
Média: {media}""")