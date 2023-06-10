# Média aritimética
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digote sua 2° nota: '))
media = (nota1 + nota2) / 2

print('\nPrimeira nota: {:.1}\nSegunda nota: {:.1}\nMédia das notas: {:.1}'.format(nota1, nota2, media))
