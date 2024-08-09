"""
12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    - Salário Bruto até 900 (inclusive) - isento
    - Salário Bruto até 1500 (inclusive) - desconto de 5%
    - Salário Bruto até 2500 (inclusive) - desconto de 10%
    - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00  
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
"""

valorHora = float(input('Digite o valor da hora de trabalho: '))
quantidadeHorasTr = float(input('Digite a quantidade de hora trabalhada no mês: '))
salarioBruto = (valorHora * quantidadeHorasTr)


def descontos(salarioBruto):
    descontoSindicato = (salarioBruto / 100) * 3
    fgts = (salarioBruto / 100) * 11
    ir = 0
    if salarioBruto <= 900:
        salarioLiquido = salarioBruto - descontoSindicato
        
    elif salarioBruto <= 1500:
        ir = (salarioBruto / 100) * 5
        salarioLiquido = salarioBruto - descontoSindicato - ir
        
    elif salarioBruto <= 2500:
        ir = (salarioBruto / 100) * 10
        salarioLiquido = salarioBruto - descontoSindicato - ir
        
    else:
        ir = (salarioBruto / 100) * 20
        salarioLiquido = salarioBruto - descontoSindicato - ir
        
    imprimeDesconto(salarioBruto, descontoSindicato, ir, fgts, salarioLiquido)

def imprimeDesconto(salarioBruto, descontoSindicato, ir, fgts, salarioLiquido):
    print(f'Salario Bruto: {salarioBruto:.2f}')
    print(f'Desconto Sindicato: { descontoSindicato:.2f}')
    print(f'Desconto IR: {ir:.2f}')
    print(f'FGTS: {fgts:.2f}')
    print(f'Salario liquido: {salarioLiquido:.2f}')

descontos(salarioBruto)