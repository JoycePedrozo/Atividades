"""
10- Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-verpertino ou N-noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor inválido!", conforme o caso. 
"""

turno = input('Diga qual o seu turno: M - matutino, V - verpertino, N - noturno \n')

if turno == 'M' or turno =='m':
    print('Bom Dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa Noite!')
else:
    print('Valor inválido!')