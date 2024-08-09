# DESAFIO 015
"""
Escreva um programa que pergunta a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
"""

dia = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de KM percorrido: "))
pago = (dia * 60) + (km * 0.15)
print("O preco a ser pago é de: {}".format(pago))
