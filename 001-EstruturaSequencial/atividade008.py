"""
8- Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
"""
salario = float(input('Digite quanto ganha por hora trabalhadas: '))
horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salarioFinal = salario * horas

print(f'Salario: {salarioFinal}')