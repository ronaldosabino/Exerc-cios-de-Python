# Catetos e hipotenusa

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite o valor do ângulo:\t'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print('\nO angulo de {}° possui...\nSeno:\t{:.2f}\nCosseno:\t{:.2f}\nTangente:\t{:.2f}'.format(angulo, sen, cos, tg))
