"""
------------------------------------ PERGUNTA

Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. 
Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 

"""

#------------------------------------ RESPOSTA

placa = input('Digite uma placa de carro, seguindo o formato: AAA-1550: ')
placa = placa.upper()

if ('-' not in placa) or (len(placa) != 8):
    print('False')
else:
    if (placa[0].isalpha() and 
        placa[1].isalpha() and 
        placa[2].isalpha() and 
        placa[3] == '-' and 
        placa[4].isalnum() and 
        placa[5].isalnum() and 
        placa[6].isalnum() and 
        placa[7].isalnum()):
        print('True')