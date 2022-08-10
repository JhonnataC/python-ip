cores = {'limpar': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m'}

def menuPrincipal():
    print()
    print('{}--- MENU PRINCIPAL ---{}\n'.format(cores['amarelo'], cores['limpar']))
    print('[1] - Menu de Clínica')
    print('[2] - Menu de Funcionário')
    print('[3] - Menu de Médico')
    print('[4] - Menu de Paciente')
    print('[5] - Menu de Marcação de Consulta')
    print('[6] - Sair')
    op = int(input('Opção: '))
    return op

def menuClinica():
    print()
    print('{}>>> MENU CLÍNICA <<<{}\n'.format(cores['amarelo'], cores['limpar']))
    print('[1] - Cadastrar Clínica')
    print('[2] - Buscar Clínica')
    print('[3] - Editar Clínica')
    print('[4] - Remover Clínica')
    print('[5] - Listar todas as Clínicas')
    print('[6] – Voltar para o menu principal')
    res = int(input('Opção: '))
    return res

def menuFuncionario():
    print()
    print('{}>>> MENU FUNCIONÁRIO <<<{}\n'.format(cores['amarelo'], cores['limpar']))
    print('[1] - Cadastrar Funcionário')
    print('[2] - Buscar Funcionário')
    print('[3] - Editar Funcionário')
    print('[4] - Remover Funcionário')
    print('[5] - Listar Todos os Funcionários')
    print('[6] - Voltar para o menu principal')
    res = int(input('Opção: '))
    return res

def menuMedico():
    print()
    print('{}>>> MENU MÉDICO <<<{}\n'.format(cores['amarelo'], cores['limpar']))
    print('[1] - Cadastrar Médico')
    print('[2] - Buscar Médico por CRM')
    print('[3] - Editar Médico')
    print('[4] - Remover Médico')
    print('[5] - Listar Todos os Médicos')
    print('[6] - Pesquisar Médico por Especialidade')
    print('[7] – Voltar para o menu principal')
    res = int(input('Opção: '))
    return res

def menuPaciente():
    print()
    print('{}>>> MENU PACIENTE <<<{}\n'.format(cores['amarelo'], cores['limpar']))
    print('[1] - Cadastrar Paciente')
    print('[2] - Listar Todos os Pacientes')
    print('[3] - Buscar Paciente por CPF') 
    print('[4] - Editar Paciente')
    print('[5] - Remover Paciente')
    print('[6] – Voltar para o menu principal')
    res = int(input('Opção: '))
    return res

def marcacaoConsulta():
    print()
    print('{}>>> MENU MARCAÇÃO DE CONSULTAS <<<{}\n'.format(cores['amarelo'], cores['limpar']))
    print('[1] - Marcar Consulta')
    print('[2] - Buscar Consulta por Paciente')
    print('[3] - Editar Consulta')
    print('[4] - Remover Consulta')
    print('[5] - Listar Consultas')
    print('[6] - Listar consultas por Retorno')
    print('[7] - Listar Consultas por intervalo de datas')
    print('[8] - Voltar para o menu principal')
    res = int(input('Opção: '))
    return res 