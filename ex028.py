# Jogo da advinhação v.10

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

aleatorio = int(randint(0, 5))
num = int(input('Digite um número: '))

print('\nEu pensei no número {}'.format(aleatorio))

if num != aleatorio:
    print('Você perdeu... Tente novamente')
else:
    print('VOCÊ VENCEU!!!')
