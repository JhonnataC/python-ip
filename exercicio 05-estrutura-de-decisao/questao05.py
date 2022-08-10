temp = float(input('Digite a temperatura: '))
print  ("[01] Celsius para Fahrengheit \n[02] Fahrengheit para celsius ")
op = int(input('Escolha uma opção: '))
if op==1:
    convert = (temp*1.8+32)
    print('A temperatura em fahrengheit é: {:.2f}'.format(convert))
elif op==2:
    convert=(temp-32)*5/9
    print('A temperatura em Celsius é : {:.2f}'.format(convert))
else :
    print('Valor inválido! ')
    
     
    


