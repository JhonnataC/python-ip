from menuAgenda import *
from funcoesAgenda import *
from time import sleep

def main():
    while True:
        opMenu = menu()    
        if opMenu == 1:
            adicionarContato()
        elif opMenu == 2:
            verContatos()
        elif opMenu == 3:
            pesquisarContato()
        elif opMenu == 4:
            editarContato()
        elif opMenu == 5:
            excluirContato()
        elif opMenu == 6:
            print('Encerrando serviço...')
            sleep(2)
            print('Obrigado...')
            break
        else:
            print('Opção inválida!')

main()