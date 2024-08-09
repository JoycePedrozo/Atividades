"""
1- Faça um programa que peça dois números e imprima o maior deles.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digigte o segundo número: '))

if n1 == n2:
    print(f'{n1} e {n2} são iguais')
elif n1 > n2:
    print(f'{n1} é maior do que {n2}')
else:
    print(f'{n2} é maior que {n1}')