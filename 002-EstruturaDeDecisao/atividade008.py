"""
8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
produto1 = float(input('Digite o valor do produto 1: '))
produto2 = float(input('Digite o valor do produto 2: '))
produto3 = float(input('Digite o valor do produto 3: '))

print(f'{produto1}, {produto2}, {produto3}')

if produto1 < produto2 and produto1 < produto3:
    print(f'O produto mais barato é o produto 1. Que custa {produto1}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'O produto mais barato é o produto 2. Que custa {produto2}')
else:
    print(f'O produto mais barato é o produto 3. Que custa {produto3}')