def questao3():
    print('======MENOR NÚMERO======')
    quantNum = int(input('Quantos números deseja digitar? '))
    menor = 0
    interacao = 1
    for i in range(1, quantNum+1):
        num = int(input('Digite um número: '))
        
        if interacao == 1: 
            menor = num
            interacao += 1
            
        if num < menor:
            menor = num
            
    print('O menor número foi {}'.format(menor))   

