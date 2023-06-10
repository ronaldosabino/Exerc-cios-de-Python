# Sorteando uma ordem na lista

# O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno:\t'))
aluno2 = str(input('Digite o nome do segundo aluno:\t'))
aluno3 = str(input('Digite o nome do terceiro aluno:\t'))
aluno4 = str(input('Digite o nome do quarto aluno:\t'))
lista = [aluno1, aluno2, aluno3, aluno4]
# random.shuffle(lista) serve para embaralhar
shuffle(lista)

print('\nA ordem de apresentação ficou assim:')
print(lista)
