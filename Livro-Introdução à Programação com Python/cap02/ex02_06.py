"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3

Site: https://python.nilo.pro.br/

Arquivo: exercicios3\capitulo 02\exercicio-02-06.py

------------------------------------ PERGUNTA

Modifique o Programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$ 750.

"""

# ------------------------------------ RESPOSTA

salario = 750
aumento = 15
print(salario + (salario * aumento / 100))

# ------------------------------------ EXPERIMENTANDO

salario = 1000
aumento = 20
print(salario*(1+(aumento/100)))
