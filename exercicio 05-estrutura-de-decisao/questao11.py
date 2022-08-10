nome1 = str(input('Digite seu nome: '))
idade1= int(input('Digite sua idade '))
if (idade1<= 10):
    print(nome1 , 'Você terá que pagar: R$30.00 reais ')
elif (idade1>=11) and (idade1<=29):
    print (nome1 , 'Você terá que pagar: R$60.00 ')
elif (idade1>=30) and (idade1)<=45:
    print (nome1 , 'Você terá que pagar: R$120.00 reais ')
elif (idade1>=46) and (idade1<=59):
    print (nome1 , 'Você terá que pagar: R$150.00 reais')
elif (idade1>=60) and (idade1<=65):
    print (nome1 , 'Você terá que pagar: R$250.00 reais ')
else:
    print (nome1 , 'Você terá que pagar: R$400.00 reais') 
        