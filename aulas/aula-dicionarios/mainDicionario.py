from controladorDicionario import *
from menuDicionario import menuApli

def main():
    while True:
        op = menuApli()
        if op == 1:
            cadastrarFuncionario()
        elif op == 2:
            listagemFuncionarios()
        elif op == 3:
            editarFuncionario()
        elif op == 4:
            excluirFuncionario()
        elif op == 5:
            print('Saindo...')
            break
        
main()