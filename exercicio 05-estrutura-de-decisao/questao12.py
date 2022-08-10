diaVenc = int(input('Informe o dia de vencimento: '))
diaPag = int(input('Dia em que o pagamento está sendo feito: '))
val = float(input('Valor da prestação: R$ '))
print(25*'=')
dif = diaPag - diaVenc

if dif < 0:
    valF = val - val*10/100
    print('Parabéns! Você ganhou 10% de desconto por ter pago antes do vencimento. \nValor final à pagar: R$ {:.2f}'.format(valF))
elif dif <= 5:
    valF = val
    print('Por pouco você não ganhou nosso desconto! \nValor final à pagar: R$ {:.2f}'.format(valF))
elif dif > 5:
    valF = val + val*((dif-5)*2)/100
    print('Como você pagou com um atraso de mais de 5 dias, recebeu uma multa de 2% por cada dia de atraso.')
    print('Porcentagem da multa: {}%'.format((dif-5)*2))
    print('Valor final à pagar: {}'.format(valF))
