# DESAFIO 004
"""
 Faça um programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
n = input('Digite algo: ')
print('É um alfabético? ', n.isalpha())
print('É um número? ', n.isnumeric())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada? ', n.isalnum())
print('Só tem espaços? ', n.isspace())