# Primeira e última ocorrência dentro de uma string

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em qual posição ela aparece a primeira vez
# Em qual posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()

# Usando o count para contar quantas vezes o caracter se repete
print('\nQuantas vezes aparece a letra "A"? {}'.format(frase.upper().count('A')))
# Usando o find para encontrar a posiçao da string mencionada
print('Em qual posição ela aparece a primeira vez? {}'.format(frase.upper().find('A')))
# Usando o rfind para encontrar a posição da string mencionada para direita
print('Em qual posição ela aparece pela ultima vez? {}'.format(frase.upper().rfind('A')))
