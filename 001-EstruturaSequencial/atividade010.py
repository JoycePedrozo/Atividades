"""
10- Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
"""
celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = celsius * 1.8 + 32

print(f'A temperatura em Celsius {celsius} convertida para Fahrenheit é {fahrenheit:.2f}')