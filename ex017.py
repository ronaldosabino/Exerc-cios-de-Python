# Catetos e hipotenusa

# Faça um programa que leia o comprimento do cateto adjacente de um triangulo retângulo
# e mostre o comprimento da hipotenusa

# math.hypot(co, ca) é o metodo dentro do modulo math que calcula hipotenusa

import math

op = float(input('Qual o comprimento do cateto oposto?\t'))
adj = float(input('Qual o comprimento do cateto adjacente?\t'))
potop = math.pow(op, 2)
potadj = math.pow(adj, 2)
raiz = (potop + potadj) ** (1/2)
# hip = math.hypot(op, adj)

print('\nA hipotenusa desse triangulo retangulo tem um comprimento de {:.2f}'.format(raiz))
# print('\nA hipotenusa desse triangulo retangulo tem um comptrimento de {:.2f}'.format(hip))