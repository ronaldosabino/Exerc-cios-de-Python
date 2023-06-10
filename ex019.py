# Sorteando um item na lista

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido

# from modulo import metodo importa apenas o metodo necessário, evitando de importar o modulo completo
from random import choice

# existe uma forma de guardar vários dados na mesma variável usando vetores, iremos aprender depois
aluno1 = str(input('Digite o nome do primeiro aluno:\t'))
aluno2 = str(input('Digite o nome do segundo aluno:\t'))
aluno3 = str(input('Digite o nome do terceiro aluno:\t'))
aluno4 = str(input('Digite o nome do quarto aluno:\t'))
# var = [] cria uma lista
lista = [aluno1, aluno2, aluno3, aluno4]
# random.choice escolhe um item da lista
sorteio = choice(lista)

print('\nHoje é o dia de {} limpar o quadro'.format(sorteio))
