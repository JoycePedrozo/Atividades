# DESAFIO 009
"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""

tabuada = int(input('Tabuada do número: '))
for count in range(10):
    print('{} + {} = {}'.format(tabuada, count + 1, tabuada + (count + 1)) )
print('\n')
for count in range(10):
    print('{} - {} = {}'.format(tabuada, count + 1, tabuada - (count + 1)) )
print('\n')
for count in range(10):
    print('{} * {} = {}'.format(tabuada, count + 1, tabuada * (count + 1)) )
print('\n')
for count in range(10):
    print('{} / {} = {}'.format(tabuada, count + 1, tabuada / (count + 1)))
