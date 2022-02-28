"""
------------------------------------ PERGUNTA

Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.

"""

#------------------------------------ RESPOSTA

estados = {"AC" : "Acre", "AL" : "Alagoas", "AP" : "Amapá" , "AM" : "Amazonas", "BA" : "Bahia", "CE" : "Ceará", "DF" : "Distrito Federal", "ES" : "Espírito Santo", "GO" : "Goiás", "MA" : "Maranhão", "MT" : "Mato Grosso", "MS" : "Mato Grosso do Sul", "MG" : "Minas Gerais", "PA" : "Pará", "PB" : "Paraíba", "PR" : "Paraná", "PE" : "Pernambuco", "PI" : "Piauí", "RR" : "Roraima", "RO" : "Rondônia", "RJ" : "Rio de Janeiro", "RN" : "Rio Grande do Norte", "RS" : "Rio Grande do Sul", "SC" : "Santa Catarina", "SP" : "São Paulo", "SE" : "Sergipe", "TO" : "Tocantins"}
sigla = input("Digite a sigla do estado: ")

print(f"O nome completo do estado é {estados[sigla.upper()]}")

# .upper() só para garantir que quando digitado, por exemplo, ms ou Ms ou MS fique sempre com o padrão MS.