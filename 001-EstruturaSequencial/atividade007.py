"""
7- Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
qua = (float(input('Lado de um quadrado em m: ')))
area = qua ** 2
dobro = area * 2
print(f'A área de um quadrado de medidas de lados {qua}m é de {area}')
print(f'O dobro desta área é de {dobro}')