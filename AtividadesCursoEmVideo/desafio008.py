# DESAFIO 008
"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida {}m correspondente a {}cm e {}mm'.format(medida,cm,mm))
