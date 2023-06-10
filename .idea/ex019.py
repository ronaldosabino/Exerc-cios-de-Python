# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lemdo o nome deles e escrevendo o nome escolhido

import random
import string

aluno1 = input('Digite o nome do primeiro aluno:\t')
aluno2 = input('Digite o nome do segundo aluno:\t')
aluno3 = input('Digite o nome do terceiro aluno:\t')
aluno4 = input('Digite o nome do quarto aluno:\t')

print('\nHoje é o dia de {} apagar o quadro'.format(random.randrange(aluno4, aluno3, aluno2, aluno1)))
