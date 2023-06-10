# dissecando uma variável
# Faça um programa que leia pelo teclado e mostre na tela o seu tipo primitivo e mais informações sobre ele

# print(type(var)) serve para descrever qual é o tipo da variável
# print(var.is()) serve para validar se a variável é alpha, num, etc

variavel2 = input('digite algo: ')
print('este é o tipo da variável', type(variavel2))
print('esta variável é numerica?', variavel2.isnumeric())
print('esta variável é alfabetica?', variavel2.isalpha())
print('esta variável é alfanumerica?', variavel2.isalnum())
print('esta variável é um espaço?', variavel2.isspace())
print('esta variável está minuscula?', variavel2.islower())
print('esta variável está maiscula?', variavel2.isupper())
