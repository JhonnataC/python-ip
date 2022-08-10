from menusApli import *
from funcoesApli import *
from time import sleep

cores = {'limpar': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m'}

def main():
    while True:
        op = menuPrincipal()
        if op == 1:
            while True:
                res = menuClinica()
                if res == 1:
                    cadastroClinica()
                elif res == 2:
                    buscarCnpj()
                elif res == 3:
                    editarClinica()
                elif res == 4:
                    excluirClinica()
                elif res == 5:
                    listarClinicas()
                elif res == 6:
                    print('\n{}Voltando para o menu principal...{}'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5)
                    break
                else:
                    print('\n{}Opção inválida!{}'.format(cores['vermelho'], cores['limpar']))
        elif op == 2:
            while True:
                res = menuFuncionario()
                if res == 1:
                    cadastroFuncionario()
                elif res == 2:
                    buscarMatricula()
                elif res == 3:
                    editarFuncionario()
                elif res == 4:
                    excluirFuncionario()
                elif res == 5:
                    listarFuncionarios()
                elif res == 6:
                    print('\n{}Voltando para o menu principal...{}'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5) 
                    break
                else:
                    print('\n{}Opção inválida!{}'.format(cores['vermelho'], cores['limpar']))
        elif op == 3:
            while True:
                res = menuMedico()
                if res == 1:
                    cadastroMedico()
                elif res == 2:
                    buscarCrm()
                elif res == 3:
                    editarMedico()
                elif res == 4:
                    excluirMedico()
                elif res == 5:
                    listarMedicos()
                elif res == 6:
                    pesquisarMedicoEspecialidade()
                elif res == 7:
                    print('\n{}Voltando para o menu principal...{}'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5)
                    break
                else:
                    print('\n{}Opção inválida!{}'.format(cores['vermelho'], cores['limpar']))
        elif op == 4:
            while True:
                res = menuPaciente()
                if res == 1:
                    cadastroPacientes()
                elif res == 2:
                    listagemPacientes()
                elif res == 3:
                    buscarCpf()
                elif res == 4:
                    editarPacientes()
                elif res == 5:
                    excluirPaciente()
                elif res == 6:
                    print('\n{}Voltando para o menu principal...{}'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5)
                    break
                else:
                    print('{}\nOpção inválida!{}'.format(cores['vermelho'], cores['limpar']))
        elif op == 5:
            while True:
                res = marcacaoConsulta()
                if res == 1:
                    marcarConsulta()
                elif res == 2:
                    buscarConsultaPaciente()
                elif res == 3:
                    editarConsulta()
                elif res == 4:
                    excluirConsulta()
                elif res == 5:
                    listarConsultas()
                elif res == 6:
                    listarConsultasRetorno()
                elif res == 7:
                    listarConsultasData()
                elif res == 8:
                    print('\n{}Voltando para o menu principal...{}'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5)
                    break
                else:
                    print('\n{}Opção inválida!{}'.format(cores['vermelho'], cores['limpar']))
        elif op == 6:
            print('\n{}Encerrando...{}'.format(cores['vermelho'], cores['limpar']))
            sleep(1.5)
            print('{}Obrigado!{}'.format(cores['azul'], cores['limpar']))
            break
        else:
            print('\n{}Opção inválida!{}'.format(cores['vermelho'], cores['limpar']))

main()