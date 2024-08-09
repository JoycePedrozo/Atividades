# DESAFIO 011
"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))

area = larg * alt
print('A dimensão de {} x {} e sua área é de {}m2²'.format(larg,alt,area))
tinta = area/2
print('Quantidade de tinta para pintar é de {}L'.format(tinta))
