"""
------------------------------------ PERGUNTA

Em um determinado país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros percorridos. 
Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado. 
Escreva um programa que demonstre o uso da sua função.

"""

# ------------------------------------ RESPOSTA

def calculo_taxi(distancia_km : float):
    tarifa_basica = 4
    tarifa_por_140m = 0.25

    distancia_m = distancia_km*1000
    return tarifa_basica + tarifa_por_140m*(distancia_m/140)

print(calculo_taxi(2.8))
