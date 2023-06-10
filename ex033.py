# Maior e menor valores

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# definindo o maior número
maior = n1
if n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3

# definindo o menor número
menor = n1
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3

print('\nO maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
