def questao2():
    print('======TABUADA COMPLETA DO 8======')
    print('=> Soma ')
    
    for i in range(1,11):
        print('{} + 8 = {}'.format(i, i+8))
    
    print('=> Subtração ')
   
    for i in range(8,19):
        print('{} - 8 = {}'.format(i, i-8))
        
    print('=> Multiplicação ')
    
    for i in range(1,11):
        print('{} X 8 = {}'.format(i, i*8))    
        
    print('=> Divisão ')
    
    for i in range(8,81,8):
        print('{} : 8 = {}'.format(i, i/8))

