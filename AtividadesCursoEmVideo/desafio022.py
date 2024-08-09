#DESAFIO 022
"""
Crie um programa que leia o nome completo e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas as letras minúsculas.
* Quantas letras ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite o seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
print(nome.find(' '))
separa = nome.split()
print(len(separa[0]))
