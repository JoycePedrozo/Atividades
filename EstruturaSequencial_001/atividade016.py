"""
16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura de tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs.: Somente são vendidos um númeor inteiro de latas
"""
tamanho = float(input('Qual a quantidade de metros a ser pintadas: '))
litros = tamanho / 3
        # 18 * 3
if tamanho % 54 == 0:
    latas = tamanho / 54
else:
    latas = int(tamanho / 54) + 1

valor = latas * 80
print(f'A quantidade de latas a ser comprado é : {litros:.2f}')
print(f'O valor a ser pago é: {valor:.2f}')