'''
UAST- Unidade Acadêmica de Serra Talhada
Introdução a Programação
Professor Zildomar Felix
Dupla: Jhonnata Carvalho Santos e João Vitor Alcântara da Silva
'''

indice = float(input('Escreva o índice de poluição: '))
if   indice< 35:
    print('O índice de poluição está agradável!')
elif indice>=35 and indice<=60:
    print('O índice está desagradável! ')
else:
    print('O índice está perigoso! ')