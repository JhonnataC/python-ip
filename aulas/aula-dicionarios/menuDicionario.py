def menuApli():
    print('\n{:^80}'.format('MENU'))
    print('{:*^80}'.format(''))
    print('[1] - Cadatrar funcionario')
    print('[2] - Listar funcionarios')
    print('[3] - Editar funcionario')
    print('[4] - Excluir funcionario')
    print('[5] - Sair')
    op = int(input('Opção: '))
    return op