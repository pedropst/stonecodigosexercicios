"""
------------------------------------ PERGUNTA

Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;

"""

# ------------------------------------ RESPOSTA

from math import log10

a = int(input("Digite um número: "))
b = int(input("Digite mais um número: "))

print(f"""Para esses dois números temos as seguintes relações:
            - A soma A+B é: {a+b}, 
            - A subtração B-A é: {b-a}, 
            - O produto AxB é: {a*b},
            - O quociente (parte inteira) A/B é: {a//b},
            - O resto da divisão A/B é: {a%b},
            - O logaritmo de A é: {log10(a)},
            - A elevado B é: {log10(b)}""")