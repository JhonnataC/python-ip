rendaA = float(input('Informe sua renda anual: R$ '))
numD = int(input('Informe seu número de dependentes: '))
rendaL = rendaA - rendaA*(numD*2)/100

if rendaL > 0 and rendaL <= 20000:
    impo = 0
elif rendaL > 20000 and rendaL < 50000:
    impo = rendaL*5/100
elif rendaL >= 50000 and rendaL <= 100000:
    impo = rendaL*10/100
else:
    impo = rendaL*15/100

print('Renda líquida: R$ {:.2f}'.format(rendaL))

if impo != 0: 
    print('Seu imposto de renda é: R$ {:.2f}'.format(impo))
else:
    print('Como sua renda líquida é inferior a R$20000,00. Você está isento do imposto.')
