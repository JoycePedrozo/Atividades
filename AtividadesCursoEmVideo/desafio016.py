# DESAFIO 016
"""
Crie um programa que leia um número qualquer pela teclado e mostre na tela a sua porção inteira.
Ex.:
Digite um número: 6.127
o número 6.127 tem a parte inteira 6.
"""
# de um jeito
"""from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado for {} e a sua porção inteira é {}'.format(num, trunc(num)))
"""
# de outro jeito
num = float(input('Digite um valor: '))
print('O valor digitado for {} e a sua porção inteira é {}'.format(num, int(num)))
