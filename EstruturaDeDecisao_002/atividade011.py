"""
11- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    -salários até R$ 280,00 (incluindo) : aumento de 20%
    -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        - O salário antes do reajuste;
        - O percentual de aumento aplicado;
        - O valor do aumento;
        - O novo salário, após o aumento.
"""
salario = float(input("Digite o salário do colaborador: R$ "))

print(f'O salário atual: -------------{salario}')

if salario <= 280.00:
    salarioN = (salario * 20)/100
    print(f'O percentual de aumento aplicado de 20% em cima do valor do salário é de: {salarioN}')
    print(f'O seu salário novo é de : ------------{salarioN + salario}')

elif salario <= 700.00:
    salarioN = (salario * 15)/100
    print(f'O percentual de aumento aplicado de 15% em cima do valor do salário é de: {salarioN}')
    print(f'O seu salário novo é de : ------------{salarioN + salario}')

elif salario < 1500.00:
    salarioN = (salario * 10)/100
    print(f'O percentual de aumento aplicado de 10% em cima do valor do salário é de: {salarioN}')
    print(f'O seu salário novo é de : ------------{salarioN + salario}')

else :
    salarioN = (salario * 5)/100
    print(f'O percentual de aumento aplicado de 15% em cima do valor do salário é de: {salarioN}')
    print(f'O seu salário novo é de : ------------{salarioN + salario}')

