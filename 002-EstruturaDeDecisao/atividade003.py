"""
3- Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever. F- Feminino, M- Masculino, Sexo Inválido.
"""

letra = input('Digite F - Feminino ou M - Masculino: ')
if letra == 'f' or letra == 'F':
    print('Feminino')
elif letra == 'm' or letra == 'M':
    print('Masculino')
else:
    print('Você digitou a letra errada')