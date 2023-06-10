# Conversor de medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

m = float(input('Uma medida em metros: '))
cm = m * 100
mm = m * 1000

print('Medida em metros: {}m\nConversão para centímetros: {}cm\nConversão para milimetros: {}mm'.format(m, cm, mm))
