"""
Parte do livro Introdução à Programação com Python
Autor: Nilo Ney Coutinho Menezes
Editora Novatec (c) 2010-2020
Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3

Site: https://python.nilo.pro.br/

Arquivo: exercicios3\capitulo 03\exercicio-03-03.py

# ------------------------------------ PERGUNTA

Complete a tabela a seguir utilizando a = True, b = False e c = True.

Expressão Resultado         Expressão Resultado
a and a   ○ True ○ False    a or c    ○ True ○ False
b and b   ○ True ○ False    b or c    ○ True ○ False
not c     ○ True ○ False    c or a    ○ True ○ False
not b     ○ True ○ False    c or b    ○ True ○ False
not a     ○ True ○ False    c or c    ○ True ○ False
a and b   ○ True ○ False    b or b    ○ True ○ False
b and c   ○ True ○ False

# ------------------------------------ RESPOSTA

Expressão Resultado     
a and a      True
b and b      False
not c        False
not b        True
not a        False
a and b      False
b and c      False
a or c       True
b or c       True
c or a       True
c or b       False
c or c       True
b or b       False

"""

# ------------------------------------ EXPERIMENTANDO

a = True
b = False
c = True

print(a and b)
print(a or b)
print(b or b)