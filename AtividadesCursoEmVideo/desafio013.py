# DESAFIO 013
"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

sal = float(input('Digite o seu salário: '))
aum = sal + (sal*15/100)
print('O seu salário atual é {}'.format(sal))
print('O seu salário com aumento de 15% é {}'.format(aum))