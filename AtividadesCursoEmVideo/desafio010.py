# DESAFIO 010
"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
Considere US$1,00 = R$3,27
"""
din = float(input('Digite um valor em real: R$ '))
conv = din / 3.27
print("Com R${:.2f} você pode comprar US${:.2f}".format(din,conv))
