# Quebrando um número

# crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

# import adiciona bibliotecas ou modulos

import math

num = float(input('Digite um número flutuante:\t'))
real = math.trunc(num)

print('\nO número {} tem a parte inteira {}'.format(num, real))
