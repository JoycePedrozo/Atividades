# EXEMPLO
test = 'This is just a simple string.'

# LEN
"""
ELA PODE SER USADA PARA ENCONTRAR O TAMANHO DE STRING CONTANDO ESPAÇOS E CARACTERES ESPECIAIS
"""
len(test)
"resultado = 29"


# REPLACE
"""
VAMOS PEGAR NOSSA STRING E SUBSTITUIR UMA PALAVRA USANDO O MÉTODO REPLACE.
"""
test = test.replace('simple', 'short')
test
"resultado = 'This is just a short string.'"


# COUNT
"""
 AGORA VAMOS CONTAR O NÚMERO DE VEZES QUE A PALAVRA ESPECIFICADA APARECE NA STRING, NESSE CASO ESTOU APENAS PROCURANDO POR UM CARACTER 'r'
"""
test.count('r')
"resultado = 2"


# FIND
"""
PODEMOS TAMBÉM ACHAR EM QUE POSIÇÃO ESTÁ CERTA LEVRA OU PALAVRA
"""
test.find('r')
"resultado = 18"
test[18]
"resultado = 'r'"


# SPLIT
"""
SEPARAR UMA STRING 
"""
test.split()
['This', 'is', 'just', 'a', 'short', 'string.']

"""
PODEMOS ESCOLHER O PONTO A SER SEPARADO
"""
test.split('a')
"resultado = ['This is just', ' short string.']"


#JOIN
"""
PARA JUNTAR NOSSA STRING SEPARADA, PODEMOS USAR O MÉTODO join
"""
' some '.join(test.split('a'))
"resultado = 'This is just some short string.'"

# MAIÚSCULO OU MINÚSCULO
## MAIÚSCULO
test.upper()
"resultado = 'THIS IS JUST A SHORT STRING.'"

## MINÚSCULO
test.lower()
"resultado = 'this is just a short string.'"

## CAPITALIZE
"""
PRIMEIRA LETRA MAIÚSUCLA DE UMA STRING MINÚSCULA
"""
test.lower().capitalize()
'This is just a short string.'

## TITLE
"""
DEIXA AS LETRAS DE CADA PALAVRA DA STRING MAIÚSCULA
"""
test.title()
"resutado = 'This Is Just A Short String.'"

## SWAPCASE
"""
O QUE FOR MAIÚSCULO VIRA MINÚSCULO E VICE-VERSA.
"""
test.swapcase()
"resultado = 'tHIS IS JUST A SHORT STRING.'"

## ISUPPER
"""
TESTE SE A STRING DADA É TOTALMENTE MAIÚSCULA
"""
'UPPER'.isupper()
"resultado = True"
'UpPEr'.isupper()
"resultado = False"

## ISLOWER
"""
TESTE SE A STRING DADA É TOTALMENTE MINÚSCULA
"""
'lower'.islower()
"resultado = True"
'Lower'.islower()
"resultado = False"

## ISTITLE
"""
TESTE SE A STRING DADA É ESTÁ COM TODAS AS PALAVRAS COM A PRIMEIRA LETRA MAIÚSCULA
"""
'This Is A Title'.istitle()
"resultado = True"
'This is A title'.istitle()
"resultado = False"


# ISALNUM
"""
CHECANDO SE A STRING É ALFA-NUMÉRICA
"""
'aa44'.isalnum()
"resultado = True"
'a$44'.isalnum()
"resultado = False"

# ISALPHA
"CHECANDO SE A STRING CONTÉM APENAS LETRAS"
'letters'.isalpha()
"resultado = True"
'letters4'.isalpha()
"resultado = False"


# ISDGIT
"""
checando se uma string contém apenas números.
"""
'306090'.isdigit()
"resultado = True"
'30-60-90'.isdigit()
"resultado = False"


# ISSPACE
"""
CHECAR SE UMA STRING CONTÉM APENAS ESPAÇOS.
"""
'   '.isspace()
"resultado = True"
''.isspace()
"resultado = False"


# LJUST
"""
PODEMOS ADICIONAR ESPAÇOS EM AMBOS OS LADOS DE UMA STRING. VAMOS ADICIONAR ESPAÇOS NO LADO DIREITO DE UMA STRING
"""
'A string.'.ljust(15)
"resultado = 'A string.      "

# RJUST
"""
ADICIONAR ESPAÇOS DO LADO ESQUERDO
"""
'A string.'.rjust(15)
"resultado = '      A string.'"

# CENTER
"""
CENTRALIZAR UMA STRING DENTRO DE ESPAÇOS
"""
'A string.'.center(15)
"resultado = '      A string.      '"