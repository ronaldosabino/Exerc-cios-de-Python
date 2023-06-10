# Aumentos múltiplos

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1.250, calcule um aumento de 10%
# Para inferiores ou iguais o aumento é de 15%

salario = float(input('Digite seu salário? R$'))

if salario > 1250:
    reajuste = (salario * (10 / 100)) + salario
    print('\nSeu salário com 10% de aumento ficou {:.2f}'.format(reajuste))
else:
    reajuste = (salario * (15 / 100)) + salario
    print('\nSeu salário com 15% de aumento ficou {:.2f}'.format(reajuste))
