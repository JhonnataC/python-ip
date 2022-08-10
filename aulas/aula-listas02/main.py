from menuApli import menu
import controladorApli

def main():
    while True:
        opMenu = menu()    
        if opMenu == 1:
            controladorApli.cadastrarAluno()
        elif opMenu == 2:
            controladorApli.listarAluno()
        elif opMenu == 3:
            controladorApli.calcuMedia()
        elif opMenu == 4:
            controladorApli.listarAprovados()
        elif opMenu == 5:
            controladorApli.listarReprovados()
        elif opMenu == 6:
            controladorApli.removerAluno()
        elif opMenu == 7:
            controladorApli.editarAluno()
        elif opMenu == 8:
            print('Encerrando...')
            break
        else:
            print('Opção inválida')

main()
