"""
6- Faça um programa que leia três números e mostre o maior deles
"""
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

print(f'{n1}, {n2}, {n3}')

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior')
elif n2 > n1 and n2 > n3:
    print(f'{n2} É maior')
else:
    print(f'{n3} É maior')