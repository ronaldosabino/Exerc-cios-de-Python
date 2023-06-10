# Radar eletrônico

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7.00 por cada km/h acima do limite

velocidade = float(input('Em quantos km/h você está? '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Vai na paz!')
else:
    print('Você foi multado!\nTerá que pagar R${:.2f}'.format(multa))
