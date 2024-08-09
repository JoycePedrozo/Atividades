"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
print('Digite um número para o dia da semana')
semana = int(input('1 - Domingo, 2 - Segunda, 3 - Terça, 4 - Quarta, 5 - Quinta, 6 - Sexta, 7 - Sábado: \n'))

if semana == 1:
    print('Domingo')
elif semana == 2:
    print('Segunda-feira')
elif semana == 3:
    print('Terça-feira')
elif semana == 4:
    print('Quarta-feira')
elif semana == 5:
    print('Quinta-feira')
elif semana == 6:
    print('Sexta-feira')
elif semana == 7:
    print('Sábado')
else:
    print('Você digitou um valor inválido')