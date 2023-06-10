# Conversor de moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere US$1.00 = R$5.11 (27/01/2023)

real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 5.11

print('\nR${:.2f} é igual a US${:.2f}'.format(real, dolar))
