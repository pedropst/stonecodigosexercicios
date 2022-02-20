"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3

Site: https://python.nilo.pro.br/

Arquivo: exercicios3\capitulo 03\exercicio-03-02.py

# ------------------------------------ PERGUNTA

Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

Expressão Resultado        Expressão Resultado
a == c    ○ True ○ False   b > a     ○ True ○ False
a < b     ○ True ○ False   c >= f    ○ True ○ False
d > b     ○ True ○ False   f >= c    ○ True ○ False
c != f    ○ True ○ False   c <= c    ○ True ○ False
a == b    ○ True ○ False   c <= f    ○ True ○ False
c < d     ○ True ○ False

# ------------------------------------ RESPOSTA

Expressão       Resultado     
a == c            False
a < b             True
d > b             False
c != f            False -> essa aqui é uma boa, mesmo valor numérico, mas será que por ser tipo diferente não é possível afirmar que são iguais?
a == b            False
b > a             True
c >= f            True -> mesma consideração feita acima
f >= c            True -> mesma consideração feita acima
c <= c            True
c <= f            True -> mesma consideração feita acima
c < d             False
"""

# ------------------------------------ EXPERIMENTANDO

c = 5.0
f = 5

print(c!=f)
print(c>=f)
print(f>=c)
print(c<=f)


# O que aprendemos hoje? Comparação é feita somente em relação aos valores, não tipos.