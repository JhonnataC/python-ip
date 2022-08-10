def questao4():
    print('======ENTRE 10 E 50======')
    numEntre = 0
    for i in range(1,11):
        num = int(input('Digite um número: '))
        
        if num > 10 and num < 50:
           numEntre += 1
        
    print('Quantidade de números entre 10 e 50: {}'.format(numEntre)) 
    


        