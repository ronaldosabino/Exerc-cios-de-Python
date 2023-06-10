# Ano bissexto

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Qual ano você deseja saber se é bissexto? '))
bi6 = (ano % 4)

if bi6 != 0:
    print('\n{} não é bissexto'.format(ano))
else:
    print('\n{} é bissexto'.format(ano))
