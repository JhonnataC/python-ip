baseFuncionarios = {}

def cadastrarFuncionario():
    print('\n{:^80}'.format('Cadastrar funcionario'))
    print('{:*^80}'.format(''))
    while True:
        while True:
            cpf = int(input('CPF: '))
            checCPF = checagemCPF(cpf)
            if checCPF == True:
                print('CPF já cadastrado no sistema.')
            else:
                break
        matricula = int(input('Matrícula: '))
        nome = str(input('Nome: '))
        salario = float(input('Salário: R$ '))

        funcionario = {'CPF': cpf, 'matricula': matricula, 'nome': nome, 'salario': salario}
        
        baseFuncionarios[cpf] = funcionario
        
        op = str(input('Deseja cadastrar mais um funcionário? [S] - SIM | [N] - NÃO ')).upper()
        if op == 'N':
            break
        
def checagemCPF(aux):
    return (aux in baseFuncionarios)


def listagemFuncionarios():
    print('\n{:^80}'.format('Listagem de funcionarios'))
    print('{:*^80}'.format(''))
    print('{:<17} {:<30}'.format('CPF', 'NOME'))
    print('{:-^40}'.format(''))    
    for funcionario in baseFuncionarios.values():
        print('{:<17} {:<30}'.format(funcionario.get('CPF'), funcionario.get('nome')))
        
def editarFuncionario():
    cpfPesquisado = int(input('CPF do funcionario que deseja editar: '))
    if checagemCPF(cpfPesquisado) == True:
        for funcionario in baseFuncionarios.values():
            if cpfPesquisado == funcionario.get('CPF'):
                cpf = int(input('Novo CPF: '))
                matricula = int(input('Nova matricula: '))
                nome = str(input('Novo nome: '))
                sal = float(input('Novo salário: '))
                funcionario = {'CPF': cpf, 'matricula': matricula, 'nome': nome, 'salario': sal}
                baseFuncionarios[cpf] = funcionario
                return
    else:
        print('CPF não encontrado no nosso sistema')
        
def excluirFuncionario():
    cpfPesquisado = int(input('CPF do funcionario que deseja deletar: '))
    if checagemCPF(cpfPesquisado) == True:
        for funcionario in baseFuncionarios.values():
            if funcionario.get('CPF') == cpfPesquisado:
                op = int(input('Deseja realmente excluir o funcionario {}? \n[1] - Sim | [2] - Não '.format(funcionario.get('nome'))))
                if op == 1:
                    del baseFuncionarios['cpf']
                else:
                    print('Retornando ao menu...')