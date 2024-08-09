# DESAFIO 012
"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco = float(input('Digite o preco do produto: '))
desc = preco - (preco * 5/100)
print('Valor do produto: {}'.format(preco))
print('Valor com desconto de 5% é : {:.2f}'.format(desc))
