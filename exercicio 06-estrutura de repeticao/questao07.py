def questao7():
        print('======LISTA INTEIROS======')
        print('Informe os números inteiros para formar uma lista, e termine com -1. ')
        a = str(input('Por favor, digite o primeiro número e aperte enter: '))
        while True:
            b = str(input('Digite mais um número: '))
            
            if b != '-1':
                a += b
            else:
                break
        print('A lista de inteiros é {}'.format(list(a)))
           
