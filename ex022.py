# Analisador de textos

# Crie um programa que leia o nome completo de uma peesoa e mostre:
# O nome com todas as letras maisculas
# O nome com todas as letras minusculas
# Quantas letras ao t0do (sem considerar espaços)
# Quantas letras tem o primeiro nome

# strip para desconsiderar caracteres inúteis
nome = str(input('Informe seu nome completo: ')).strip()

# USANDO O UPPER PARA TRANSFORMAR TODOS OS CARACTERES EM CAIXA ALTA
print('\nO nome com todas as letras maiúsculas: {}'.format(nome.upper()))
# usando o lower para transfomrar todos os caracteres em caixa baixa
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
# Usando o len para contar quantos caracteres existem na string, subtraindo pela quantidade de espaços com o count
print('Quantas letras tem o nome ao todo: {}'.format(len(nome) - nome.count(' ')))
# Usando o split para dividir a string levando em consideração os espaços e especificando o item da lista
print('Quantas letras tem o primeiro nome: {}'.format(len(nome.split()[0])))
