"""
11- Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a) O produto do dobro do primeiro com metade do segundo.
    b) A soma do triplo do primeiro com o terceiro.
    c) O terceiro elevado ao cubo.
"""
n1 = int(input('Digite um númeor inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
n3 = float(input('Digite um número real: '))

a = (n1 * 2) * (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevaddo ao cubo: {c:.2f}')