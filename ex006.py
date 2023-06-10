# Dobro, Triplo e raiz quadrada
# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada

# :.2f faz com que exiba apenas duas casas decimais
# pow(n, 1/2) é outra forma de calcular raiz quadrada

n1 = float(input('Digite um número: '))
print('O número digitado foi: {}\nO dobro é: {}\nO triplo é: {}\nA raiz quadrada é: {:.2f}'
      .format(n1, n1 * 2, n1 * 3, n1**(1/2)))
