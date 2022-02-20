"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3

Site: https://python.nilo.pro.br/

Arquivo: exercicios3\capitulo 03\exercicio-03-05.py

# ------------------------------------ PERGUNTA

Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir.

A  B C     D      Resultado
1  2 True  False
10 3 False False
5  1 True  True

# ------------------------------------ RESPOSTA

A  B C     D      Resultado
1  2 True  False     False
10 3 False False     False
5  1 True  True      True

"""

# ------------------------------------ EXPERIMENTANDO

# print(10 > 3 and False or True)

# O que aprendemos hoje? Verificando a precedencia das operações em: https://docs.python.org/pt-br/3/reference/expressions.html#grammar-token-python-grammar-expression
# Tem-se que as expressões são lidas da esquerda para direita, e todos os operadores possuem mesma precedencia quando não há sintaxe explicíta mudando isso, como ().
# #CONFIRMARCOMPROF -> Realmente a precedencia é a mesma para todos? Mesmo quando a expressão possui >=, AND, OR, etc.?
