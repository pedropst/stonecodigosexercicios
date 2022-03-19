"""
------------------------------------ PERGUNTA

Escreva uma função que, dado três comprimentos de retas quaisquer, diga se essas três retas podem ou não formar um triângulo, retornando true em caso positivo e false em caso negativo.
Dica n°1: Se algum dos comprimentos for negativo ou zero, não é possível formar um triângulo.
Dica n°2: se qualquer um dos comprimentos for maior ou igual à soma dos outros dois, então os comprimentos não podem ser usados para formar um triângulo. 
Caso contrário, eles podem formar um triângulo.

"""

# ------------------------------------ RESPOSTA

def triangulo(l1 : float, l2 : float, l3 : float):
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return False
    elif l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
        return False
    else:
        return True

print(triangulo(3, 4, 5))
print(triangulo(-1, 4, 5))
print(triangulo(1, 6, 5))
        