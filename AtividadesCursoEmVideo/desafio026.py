#DESAFIO 026
"""
Faça um programa que leia uma frase pelo teclado e mostre:
* Quantas vezes aparece a letra "A".
* Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez
"""
text = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(text.count('A')))
print('A primeira letra A apareceu na posição {}'.format(text.find('A')+1))
print('A última letra A apareceu na posição {}'.format(text.rfind('A')+1))