# Primeiro e último nome de uma pessoa

# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida seu primeiro e o ultimo nome separadamente
# Ex: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

nome = str(input('Digite seu nome completo: ')).strip()

print('\nPrimeiro nome: {}'.format(nome.split()[0]))
# usando split()[-1] para encontra o ultimo termo da lista
print('\nÚltimo nome: {}'.format(nome.split()[-1]))
