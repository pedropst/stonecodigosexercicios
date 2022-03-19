"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3

Site: https://python.nilo.pro.br/

Arquivo: exercicios3\capitulo 03\exercicio-03-08.py

# ------------------------------------ PERGUNTA

Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

"""

# ------------------------------------ RESPOSTA

valor_em_metros = float(input('Digite um valor em metros que será convertido para mm:'))
valor_em_mm = valor_em_metros*1000

print(f'O valor em mm é: {valor_em_mm:.2f}')