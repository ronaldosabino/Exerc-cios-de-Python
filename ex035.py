# Análisando triângulo

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

ab = float(input('Qual o comprimento da segmento "AB" em cm? '))
cd = float(input('Qual o comprimento do segmento "CD" em cm? '))
ef = float(input('Qual o comprimento do segmento "EF" em cm? '))

if ab + cd > ef and cd + ef > ab and ab + ef > cd:
    print('\nÉ possível formar um triângulo')
else:
    print('\nNão é possível formar um triângulo')
