"""
4- Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input("Digite uma letra: ")
vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

if letra in vogais:
    print('É vogal')
else:
    print('É consoante')
    