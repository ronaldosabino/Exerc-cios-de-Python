# Verificando as primeiras linhas de um texto

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

cidade = str(input('Informe o nome da cidade: ')).strip()

# usando '' in para retornar verdadeiro ou falso na divisão feita pelo split
print('\nO nome da cidade começa com "SANTO"? {}'.format('SANTO' in cidade.upper().split()[0]))
