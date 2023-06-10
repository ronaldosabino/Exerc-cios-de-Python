# Calculando descontos
# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto:\tR$'))
formula = preco * 5 / 100
desconto = preco - formula

print('\nO produto tem o valor total de R${} com 5% de desconto'.format(desconto))