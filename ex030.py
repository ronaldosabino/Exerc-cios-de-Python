# Par ou ímpar

# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

numero = int(input('Digite um número: '))
calculo = numero % 2

if calculo == 0:
    print('\nO {} número é par'.format(numero))
else:
    print('\nO {} número é ímpar'.format(numero))
