"""
5- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por um aluno e apresentar:
    * A mensagem "Aprovada", se a média alcançada for maior ou igual a sete;
    * A mensagem "Reprovado", se a média alcançada for menor do que sete;
    * A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media == 10.0:
    print(f'A sua média é {media}')
    print('Aprovado com Distinção')

elif media >= 7.0 and media <= 9.9:
    print(f'A sua média é {media}')
    print('Aprovada')
elif media <= 7.0:
    print(f'A sua média é {media}')
    print('Reprovado')
