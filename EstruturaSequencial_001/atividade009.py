"""
9- Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre em graus Celsius.
    C = 5 * ((F-32)/9).
"""
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = 5 * ((fahrenheit - 32)/9)

print(f'A temperatura Fahrenheit {fahrenheit} convertida para Celsius é {celsius:.2f}')