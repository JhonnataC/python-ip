from funcoes import executar, particao
from questao01 import questao1
from questao02 import questao2
from questao03 import questao3
from questao04 import questao4
from questao05 import questao5
from questao06 import questao6
from questao07 import questao7
from questao08 import questao8

def menu():
    while True:
        print('======MENU DE QUESTÕES======')

        for i in range(1,9):
            print('[{}] - Questão {}'.format(i, i))
        print('[9] - Sair')
        res = int(input('Digite o número da questão que deseja: '))

        if res == 1:
            executar(res)
            questao1()
            particao()
        elif res == 2:
            executar(res)
            questao2()
            particao()
        elif res == 3:
            executar(res)
            questao3()   
            particao()
        elif res == 4:
            executar(res)
            questao4()
            particao()
        elif res == 5:
            executar(res)
            questao5()
            particao()
        elif res == 6:
            executar(res)
            questao6()
            particao()
        elif res == 7:
            executar(res)
            questao7()
            particao()
        elif res == 8:
            executar(res)
            questao8()
            particao()
        elif res == 9:
            break
        else: 
            print('Opção inválida!')
    
menu()

