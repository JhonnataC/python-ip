hab = None
idade = int(input('Informe sua idade: '))

if idade > 0 and idade <= 15: 
    lic = str(input('Você poderá pescar com a licença dos seus pais. Eles tem licença? Sim/Não '))
    if lic == 'Sim' or lic == 'sim':
        hab = True
    else:
        hab = False
else:
    lic = str(input('Você já possui uma licença? Sim/Não ')) 
    if lic == 'Sim' or lic == 'sim':
        hab = True
    else:
        hab = False

if hab:
    print('Parabéns! Você está apto para pescar!')
else:
    print('Infelizmente você não está apto para pescar!')

