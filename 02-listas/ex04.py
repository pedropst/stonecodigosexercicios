"""
------------------------------------ PERGUNTA

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso): Exemplo de saída:
>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho

"""

#------------------------------------ RESPOSTA

temperaturas = []
for i in range(0, 12):
    temperaturas.append(float(input(f"Digite a temperatura do mês {i+1}: ")))

temp_media = sum(temperaturas)/12

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(f"Meses com temperatura acima da média anual de {temp_media}°")
for t in temperaturas:
    if t >= temp_media:
        print(f"{temperaturas.index(t) + 1} - {meses[temperaturas.index(t)]}")