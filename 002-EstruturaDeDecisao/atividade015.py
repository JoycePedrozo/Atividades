"""
15- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    - Triângulo Equilátero: três lados iguais;
    - Triângulo Isósceles: quaisquer dois lados iguais;
    - Triângulo Escaleno: três lados diferentes;
"""
lado1 = float(input('Digite o valor do primeiro lado do triângulo: '))
lado2 = float(input('Digite o valor do segundo lado do triângulo: '))
lado3 = float(input('Digite o valor do terceiro lado do triângulo: '))
print('')

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Os valores podem formar um triângulo.')
    if lado1 == lado2 == lado3:
        print('O triângulo é equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os valores não podem formar um triângulo.')