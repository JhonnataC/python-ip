pFab = int(input('Informe o preço de fábrica: '))
pRev = 25*pFab/100
imp = 45*pFab/100
pCon = pFab + pRev + imp
print('O custa para o consumidor será de R$ {:.2f}'.format(pCon))