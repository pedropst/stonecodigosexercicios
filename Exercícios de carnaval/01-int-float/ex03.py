"""
------------------------------------ PERGUNTA

No exercício 02 você calculou a área de um triângulo a partir da sua base e altura. 
Faça um programa que receba os 3 lados de um triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.

"""

# ------------------------------------ RESPOSTA

from math import sqrt

s1 = float(input("Insira o tamanho do lado 1 do triângulo: "))
s2 = float(input("Insira o tamanho do lado 2 do triângulo: "))
s3 = float(input("Insira o tamanho do lado 3 do triângulo: "))

s = (s1 + s2 + s3)/2
area = sqrt(s*(s-s1)*(s-s2)*(s-s3))

print(f"A área do triângulo é: {area} unidades²")