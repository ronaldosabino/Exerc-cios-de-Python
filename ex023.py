# Separando digitos de um número

# Faça um programa que leia um número inteiro de 0 até 9999 e mostre na tela cada um dos digitos separados
# Ex: 1834
# unidade: 1
# dezena: 8
# centena: 3
# milhar: 4

# NÃO USEI O MÉTODO MATEMÁTICO

numero = str(input('\nDigite um número de 0 até 9999: ')).strip()

print('Unidade: {}'.format(numero[0]))
print('Dezena: {}'.format(numero[1]))
print('Centena: {}'.format(numero[2]))
print('Milhar: {}'.format(numero[3]))
