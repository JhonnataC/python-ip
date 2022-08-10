print('Informe os dados abaixo para calcularmos a conta')
piz = int(input('Quantidade de pizzas: '))
adi = int(input('Qauntidade de adicionais: '))
ref = int(input('Quantidade de copos de refri: '))
cont = (piz * 10) + (adi * 1.50) + (ref * 0.80)
gor = 10 * cont / 100
tot = cont + gor
print('='*20)
print('Valor da conta: R$ {} \nValor da gorjeta (10%): R$ {} \nTotal à pagar: R$ {}'.format(cont, gor, tot))