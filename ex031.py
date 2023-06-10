# Custo da viagem

# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km
# e R$0.45 para viagens mais longas

distancia = float(input('Quantos km você viajou? '))

if distancia <= 200:
    print('\nO valor da sua passagem é de {}'.format(distancia * 0.50))
else:
    print('\nO valor da sua passagem é de {}'.format(distancia * 0.45))
