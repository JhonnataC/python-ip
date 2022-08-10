def questao8():
    somaNum = 0
    quantNum = 0
    print('======MÉDIA DA LISTA======')
    print('informe a lista: ', end='')
    
    while True:
        num = float(input())
        somaNum += num
        quantNum += 1
        res = str(input('Deseja continuar? S - Sim e N - Não: '))
        if res.upper() == 'N':
            break
    
    med = somaNum/quantNum
    print('Há {} números na lista.'.format(quantNum))
    print('E a média é igual {}'.format(med))
