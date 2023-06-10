# Procurando uma string dentro de outra

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome: '))

# Usando '' in variável para retornar verdadeiro ou falso
print('\nTem "Silva" no nome?', 'SILVA' in nome.upper())
