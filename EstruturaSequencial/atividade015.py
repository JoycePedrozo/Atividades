"""
15- Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a) Salário bruto
    b) Quanto pagou ao INSS
    c) Quanto pagou ao sindicato
    d) O saário líquido,
    e) Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    
    + Salário BRuto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato(5%) : R$
    = Saláio Liquido : R$
    
    Obs.: Salário Bruto - Desconto = Sa;ário Líquido
"""
ganhaPorHora = float(input('Digite quanto você ganha por hora trabalhada: '))
horasTrabalhadas = float(input('Digite quantas horas trabalhadas no mês: '))

salarioBruto = ganhaPorHora * horasTrabalhadas
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - IR - INSS - sindicato

print(f'+ Salário Bruto: R$ {salarioBruto}')
print(f'- IR (11%) : R$ {IR:.2f}')
print(f'- INSS (8%) : R$ {INSS:.2f}')
print(f'- Sindicato (5%) : R$ {sindicato:.2f}')
print(f'= Salário Liquido : R$ {salarioLiquido}')
