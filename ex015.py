# Aluguel de carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado

km = float(input('Quantos KM você percorreu com o carro?\t'))
dia = int(input('Por quantos dias você alugou o carro?\t'))
preco = (dia * 60) + (km * 0.15)

print('\nVocê precisa pagar R${:.2f}'.format(preco))
