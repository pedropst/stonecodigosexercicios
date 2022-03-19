"""
------------------------------------ PERGUNTA

Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4 
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

"""

#------------------------------------ RESPOSTA
# 0 1 2  1
# 3 4 5  2
# 6 7 8  3
def fazQuadradoMagico(tamanho=3 : int):
    lista = []
    def somadorDeLinhas(tamanho=3 : int, linha : int):
        return lista[len(lista)/tamanho] + lista[linha] + lista[linha+1]


    def somadorDeColunas():
        pass


    def somadorDeDiagonais():
        pass