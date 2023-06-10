# Pintando parede
# Faça um programa que leia a altura e a largura de uma parede em metros.
# Calcule a sua área e a quantidade necessária de tinta para pinta-la.
# Sabendo que cada litro de tinta pinta uma área de 2m²

# '\t' serve para cirar um espaçamento no print

altura = float(input('Quantos metros sua parede tem de altura?\t'))
largura = float(input('Quantos metros sua parede tem de largura?\t'))
area = altura * largura
tinta = area * 0.5

print('\nSua parede tem {:.2f}m², será necessário {:.2f}L de tinta para pinta-la'.format(area, tinta))
