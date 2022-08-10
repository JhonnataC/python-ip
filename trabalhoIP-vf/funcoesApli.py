import json
import os
from time import sleep
from datetime import date, datetime

cores = {'limpar': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m'}
#area do menu de clinica
baseClinicas = {}

def carregarClinicas():
    if os.path.exists('baseClinicas.json'):
        with open('baseClinicas.json', 'r') as arqJson:
            global baseClinicas
            baseClinicas = json.load(arqJson)
    else:
        with open('baseClinicas.json', 'w') as arqJson:
            json.dump(baseClinicas, arqJson, indent=4)

def gravarDadosClinicasJSON():
    with open('baseClinicas.json', 'w') as arqJson:
        json.dump(baseClinicas, arqJson, indent=4)
     
def lerDadosClinicasJSON():
    with open('baseClinicas.json', 'r') as arqJson:
        global baseClinicas
        baseClinicas = json.load(arqJson)

def checagemCnpj(aux):
    return aux in baseClinicas

def cadastroClinica():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'NOVA CLÍNICA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    carregarClinicas()
    while True:
        while True:
            cnpj = input('Informe o CNPJ: ')
            if checagemCnpj(cnpj):
                print('{} \nEste CNPJ já está cadastrado! Informe um CNPJ válido! \n{}'.format(cores['vermelho'], cores['limpar']))
            else:
                break
        nome = input('Informe o nome da clínica: ')
        endereco = input('Informe a cidade que se encontra a clínica: ')
        baseClinicas[cnpj] = {'cnpj': cnpj, 'nome': nome, 'endereco': endereco}
        print('{} \nCadastro realizado com sucesso! \n{}'.format(cores['verde'], cores['limpar']))
        opcao = int(input('Deseja continuar cadastrando? [1] - Sim | [2] - Não '))
        if opcao != 1: 
            break
    gravarDadosClinicasJSON()
        
def buscarCnpj():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'BUSCAR CLÍNICA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosClinicasJSON()
    CNPJVerif = input('CNPJ da clínica que deseja encontrar: ')
    if checagemCnpj(CNPJVerif):
        for clinica in baseClinicas.values():
            if clinica['cnpj'] == CNPJVerif:
                print('\n{}{:<12} {:<15} {:<15}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', 'ENDEREÇO', cores['limpar']))
                print('{:<12} {:<15} {:<15}'.format(clinica['cnpj'], clinica['nome'], clinica['endereco']))
    else:
        print('{}\nCNPJ não encontrado!{}'.format(cores['vermelho'], cores['limpar']))
       
def editarClinica():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EDITAR CLÍNICA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosClinicasJSON()
    CNPJVerif = input('CNPJ da clínica que deseja editar: ')
    if checagemCnpj(CNPJVerif):
        for clinica in baseClinicas.values():
            if clinica['cnpj'] == CNPJVerif:
                print('\n{}{:<12} {:<15} {:<15}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', 'ENDEREÇO', cores['limpar']))
                print('{:<12} {:<15} {:<15}'.format(clinica['cnpj'], clinica['nome'], clinica['endereco']))
                opcao = int(input('\nQuer realmente editar? [1] - Sim | [2] - Não '))
                if opcao == 1:
                    while True:
                        novoCnpj = input('Novo CNPJ: ')
                        if checagemCnpj(novoCnpj):
                            print('{} \nEste CNPJ já está cadastrado! Informe um CNPJ válido! \n{}'.format(cores['vermelho'], cores['limpar']))
                        else:
                            break
                    novoNome = input('Novo nome da clínica: ')
                    novoEndereco = input('Novo endereço: ')
                    baseClinicas[novoCnpj] = {'cnpj': novoCnpj, 'nome': novoNome, 'endereco': novoEndereco}
                    del baseClinicas[CNPJVerif]
                    print('{} \nDados editados com sucesso! {}'.format(cores['verde'], cores['limpar']))
                    gravarDadosClinicasJSON()
                    return
                else:
                    print('{} \nEdição cancelada {}'.format(cores['amarelo'], cores['limpar']))
                    return

def excluirClinica():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EXCLUIR CLÍNICA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosClinicasJSON()
    CNPJVerif = input('Informe o CNPJ da clínica que deseja excluir: ')
    if checagemCnpj(CNPJVerif):
        for clinica in baseClinicas.values():
            if clinica['cnpj'] == CNPJVerif:
                print('{}{:<12} {:<15} {:<15}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', 'ENDEREÇO', cores['limpar']))
                print('{:<12} {:<15} {:<15}'.format(clinica['cnpj'], clinica['nome'], clinica['endereco']))
                opcao = int(input('\nDeseja realmente excluir esta clínica? [1] - Sim | [2] - Não '))
                if opcao == 1:
                    del baseClinicas[CNPJVerif]
                    print('{}\nClinica excluída com sucesso!\n{}'.format(cores['verde'], cores['limpar']))
                    gravarDadosClinicasJSON()
                    return
                else:
                    print('{}\nProcesso cancelado{}'.format(cores['amarelo'], cores['limpar']))
                    return

def listarClinicas():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'LISTAGEM DE CLÍNICAS', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosClinicasJSON()
    print('{}{:<12} {:<15} {:<15}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', 'ENDEREÇO', cores['limpar']))
    for clinica in baseClinicas.values():
        print('{:<12} {:<15} {:<15}'.format(clinica['cnpj'], clinica['nome'], clinica['endereco']))
   
        
#area do menu de funcionario
baseFuncionarios = {}

def carregarFuncionarios():
    if os.path.exists('baseFuncionarios.json'):
        with open('baseFuncionarios.json', 'r') as arqJson:
            global baseFuncionarios
            baseFuncionarios = json.load(arqJson)
    else:
        with open('baseFuncionarios.json', 'w') as arqJson:
            json.dump(baseFuncionarios, arqJson, indent=4)

def gravarDadosFuncionariosJSON():
    with open('baseFuncionarios.json', 'w') as arqJson:
        json.dump(baseFuncionarios, arqJson, indent=4)
     
def lerDadosFuncionariosJSON():
    with open('baseFuncionarios.json', 'r') as arqJson:
        global baseFuncionarios
        baseFuncionarios = json.load(arqJson)

def checagemMatricula(aux):
    return aux in baseFuncionarios

def checagemCPF(aux):
    return aux in baseFuncionarios

def cadastroFuncionario():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'NOVO FUNCIONÁRIO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    carregarFuncionarios()
    lerDadosClinicasJSON()
    while True:
        while True:
            matricula = str(input('Sua matricula: '))
            if checagemMatricula(matricula) == True:
                print('{} \nEssa matricula já existe no nosso sistema! Digite uma matricula válida para continuar \n{}'.format(cores['vermelho'], cores['limpar']))
            else:
                break
        while True:
            cpf = str(input('Seu CPF: '))
            if checagemCPF(cpf) == True:
                print('{} \nEste CPF já existe no nosso sistema! Digite um CPF válido para continuar \n{}'.format(cores['vermelho'], cores['limpar']))
            else:
                break
        nome = str(input('Nome: '))
        email = str(input('E-mail: '))
        print('\n{}Clínicas disponiveis: {}'.format(cores['amarelo'], cores['limpar']))
        print('\n{}{:<12} {:<12}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', cores['limpar']))
        for clinica in baseClinicas.values():
            print('{:<12} {:<12}'.format(clinica['cnpj'], clinica['nome']))
        clinica = str(input('\nInforme o nome da clínica: '))       
        baseFuncionarios[matricula] = {'matricula': matricula,'cpf': cpf, 'nome': nome, 'email': email, 'clinica': clinica}
        print('{}\nCadastro realizado com sucesso!{}\n'.format(cores['verde'], cores['limpar']))
        opcao = int(input('Deseja continuar cadastrando? [1] - Sim | [2] - Não \nOpção: '))
        if opcao != 1:
            break
    gravarDadosFuncionariosJSON()
     
def buscarMatricula():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'BUSCAR FUNCIONÁRIO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosFuncionariosJSON()
    matriculaVerif = input('Matricula do Funcionário que deseja buscar: ')
    if checagemMatricula(matriculaVerif):
        for funcionario in baseFuncionarios.values():
            if funcionario['matricula'] == matriculaVerif:
                print('\n{}{:<12} {:<12} {:<12} {:<12} {:<12}{}'.format(cores['amarelo'], 'MATRICULA','CPF', 'NOME', 'E-MAIL','CLÍNICA', cores['limpar']))
                print('{:<12} {:<12} {:<12} {:<12} {:<12}'.format(funcionario['matricula'], funcionario['cpf'], funcionario['nome'], funcionario['email'], funcionario['clinica']))
    else:
        print('{}\nMatricula não encontrado!{}'.format(cores['vermelho'], cores['limpar']))
        
def editarFuncionario():  
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EDITAR FUNCIONÁRIO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosClinicasJSON()
    lerDadosFuncionariosJSON()
    matriculaVerif = input('Matricula do Funcionário que deseja buscar: ')
    if checagemMatricula(matriculaVerif):
        for funcionario in baseFuncionarios.values():
            if funcionario['matricula'] == matriculaVerif:
                print('\n{}{:<12} {:<12} {:<12} {:<12} {:<12}{}'.format(cores['amarelo'], 'MATRICULA','CPF', 'NOME', 'E-MAIL','CLÍNICA', cores['limpar']))
                print('{:<12} {:<12} {:<12} {:<12} {:<12}'.format(funcionario['matricula'], funcionario['cpf'], funcionario['nome'], funcionario['email'], funcionario['clinica']))             
                opcao = int(input('\nDeseja editar? [1]- Sim [2]- Não  '))               
                if opcao == 1 :
                    while True:
                        novaMatricula = input('Escreva uma nova matricula: ')
                        if checagemMatricula(novaMatricula):
                            print('{}\nEssa Matricula já existe no nosso sistema! Digite uma Matricula válida para continuar \n{}'.format(cores['vermelho'], cores['limpar']))
                        else:
                            break
                    while True:
                        novoCpf = input('Escreva um novo CPF: ')
                        if checagemCPF(novoCpf):
                            print('{}\nEste CPF já existe no nosso sistema! Digite um CPF válido para continuar \n{}'.format(cores['vermelho'], cores['limpar']))
                        else:
                            break
                    novoNome = input('Escreva um novo nome: ')
                    novoEmail = input('Escreva um novo email: ')
                    print('{}\nClínicas disponiveis: {}'.format(cores['amarelo'], cores['limpar']))
                    print('{}{:<12} {:<12}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', cores['limpar']))
                    for clinica in baseClinicas.values():
                        print('{:<12}  {:<12}'.format(clinica['cnpj'], clinica['nome']))
                    novaClinica = input('\nEscreva uma nova clínica: ')
                    funcionario = {'matricula': novaMatricula,'cpf': novoCpf, 'nome': novoNome, 'email':novoEmail, 'clinica': novaClinica}
                    baseFuncionarios[novaMatricula] = funcionario
                    del baseFuncionarios[matriculaVerif]
                    print('{}\nDados editados com sucesso! \n{}'.format(cores['verde'], cores['limpar']))
                    gravarDadosFuncionariosJSON()
                    return           
    else:
        print('{}\nA Matricula não foi encontrada! \n{}'.format(cores['vermelho'], cores['limpar']))     

def excluirFuncionario():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EXCLUIR FUNCIONÁRIO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosFuncionariosJSON()
    matriculaVerif = input('Matricula do funcionário que deseja excluir: ')
    if checagemMatricula(matriculaVerif):
        for funcionario in baseFuncionarios.values():
            if funcionario['matricula'] == matriculaVerif:
                print('\n{}{:<12} {:<12} {:<12} {:<12} {:<12}{}'.format(cores['amarelo'], 'MATRICULA','CPF', 'NOME', 'E-MAIL','CLÍNICA', cores['limpar']))
                print('{:<12} {:<12} {:<12} {:<12} {:<12}'.format(funcionario['matricula'], funcionario['cpf'], funcionario['nome'], funcionario['email'], funcionario['clinica']))             
                opcao = int(input('Deseja excluir este funcionário? [1]- Sim | [2]- Não '))
                if opcao == 1:
                    del baseFuncionarios[matriculaVerif] 
                    print('{}\nFuncionário excluído com sucesso! {}'.format(cores['verde'], cores['limpar']))
                    gravarDadosFuncionariosJSON()
                    return
    else:
        print('{}\nA Matricula não encontrada! {}'.format(cores['vermelho'], cores['limpar']))

def listarFuncionarios():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'LISTAGEM DE FUNCIONÁRIOS', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosFuncionariosJSON()
    print('{}{:<12} {:<12} {:<12} {:<12} {:<12}{}'.format(cores['amarelo'], 'MATRICULA','CPF', 'NOME', 'E-MAIL', 'CLÍNICA', cores['limpar']))
    for funcionario in baseFuncionarios.values():
         print('{:<12} {:<12} {:<12} {:<12} {:<12}'.format(funcionario['matricula'], funcionario['cpf'], funcionario['nome'], funcionario['email'], funcionario['clinica']))
         
         
#area do menu de medico
baseMedicos = {}

def carregarMedicos():
    if os.path.exists('baseMedicos.json'):
        with open('baseMedicos.json', 'r') as arqJson:
            global baseMedicos
            baseMedicos = json.load(arqJson)
    else:
        with open('baseMedicos.json', 'w') as arqJson:
            json.dump(baseMedicos, arqJson, indent=4)

def gravarDadosMedicosJSON():
    with open('baseMedicos.json', 'w') as arqJson:
        json.dump(baseMedicos, arqJson, indent=4)
     
def lerDadosMedicosJSON():
    with open('baseMedicos.json', 'r') as arqJson:
        global baseMedicos
        baseMedicos = json.load(arqJson)

def checagemCrm(aux):
    return aux in baseMedicos

def cadastroMedico():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'NOVO MÉDICO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    carregarMedicos()
    lerDadosClinicasJSON()
    while True:
        while True:
            crm = input('Informe seu CRM: ')
            if checagemCrm(crm):
                print('{}\nEste CRM já está cadastrado! Informe um CRM válido! \n{}'.format(cores['vermelho'], cores['limpar']))
            else:
                break
        nome = input('Seu nome: ')
        email = input('Seu E-mail: ')
        while True:
            especialidade = input('[C] - Cardiologia \n[N] - Neurologia \nSua especialidade: ').upper()
            if especialidade == 'C':
                especialidade = 'Cardiologia'
                break
            elif especialidade == 'N':
                especialidade = 'Neurologia'
                break
            else:
                print('{}\nOpção inválida! \n{}'.format(cores['vermelho'], cores['limpar']))
        print('\n{}{:<12} {:<12}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', cores['limpar']))
        for clinica in baseClinicas.values():
            print('{:<12} {:<12}'.format(clinica['cnpj'], clinica['nome']))
        clinica = input('\nInforme a sua clínica com o nome: ')
        baseMedicos[crm] = {'crm': crm, 'nome': nome, 'email': email, 'especialidade': especialidade, 'clinica': clinica}
        print('{}\nCadastro realizado com sucesso! \n{}'.format(cores['verde'], cores['limpar']))
        opcao = int(input('Deseja continuar cadastrando? [1] - Sim | [2] - Não '))
        if opcao != 1:
            break
    gravarDadosMedicosJSON()   
    
def buscarCrm():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'BUSCAR MÉDICOS', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosMedicosJSON()
    CRMverif = input('CRM do médico que desejar buscar: ')
    if checagemCrm(CRMverif):
        for medico in baseMedicos.values():
            if medico['crm'] == CRMverif:
                print('\n{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
                print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medico['crm'], medico['nome'], medico['email'], medico['especialidade'], medico['clinica']))
    else:
        print('{}\nCRM não encontrado! \n{}'.format(cores['vermelho'], cores['limpar']))            
                
def editarMedico():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EDITAR MÉDICO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosMedicosJSON()
    lerDadosClinicasJSON()
    CRMVerif = input('CRM do médico que deseja editar: ')
    if checagemCrm(CRMVerif):
        for medico in baseMedicos.values():
            if medico['crm'] == CRMVerif:
                print('\n{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
                print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medico['crm'], medico['nome'], medico['email'], medico['especialidade'], medico['clinica']))
                opcao = int(input('Deseja editar? [1] - Sim | [2] - Não '))
                if opcao == 1:
                    while True:
                        novoCrm = input('Novo CRM: ')
                        if checagemCrm(novoCrm):
                            print('{}\nEste CRM já está cadastrado! Informe um CRM válido!\n{}'.format(cores['vermelho'], cores['limpar']))
                        else:
                            break
                    novoNome = input('Novo nome: ')
                    novoEmail = input('Novo E-mail: ')
                    novaEspecialidade = input('[C] - Cardiologia \n[N] - Neurologia \nNova especialidade: ').upper()
                    while True:
                        if novaEspecialidade == 'C':
                            novaEspecialidade = 'Cardiologia'
                            break
                        elif novaEspecialidade == 'N':
                            novaEspecialidade = 'Neurologia'
                            break
                        else:
                            print('{}\nOpção inválida!\n{}'.format(cores['vermelho'], cores['limpar']))
                    print('\n{}{:<12} {:<15}{}'.format(cores['amarelo'], 'CNPJ', 'CLÍNICA', cores['limpar']))
                    for clinica in baseClinicas.values():
                        print('{:<12} {:<15}'.format(clinica['cnpj'], clinica['nome']))
                    novaClinica = input('\nNova clínica: ')
                    medico = {'crm': novoCrm, 'nome': novoNome, 'email': novoEmail, 'especialidade': novaEspecialidade, 'clinica': novaClinica}
                    baseMedicos[novoCrm] = medico
                    del baseMedicos[CRMVerif]
                    print('{}\nDados editados com sucesso!{}'.format(cores['verde'], cores['limpar']))
                    gravarDadosMedicosJSON()
                    return
    else:
        print('{}\nCRM não encontrado!{}'.format(cores['vermelho'], cores['limpar']))

def excluirMedico():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EXCLUIR MÉDICO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosMedicosJSON()
    CRMVerif = input('Digite o CRM do médico que deseja excluir: ')
    if checagemCrm(CRMVerif):
        for medico in baseMedicos.values():
            if medico['crm'] == CRMVerif:
                print('\n{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
                print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medico['crm'], medico['nome'], medico['email'], medico['especialidade'], medico['clinica']))
                opcao = int(input('Deseja excluir? [1] - Sim | [2] - Não '))
                if opcao == 1:
                    del baseMedicos[CRMVerif]  
                    print('{}\nMédico excluido com sucesso!{}'.format(cores['verde'], cores['limpar']))  
                    gravarDadosMedicosJSON()
                    return
                
def listarMedicos():
    print()
    print('{} >>> LISTAGEM DE MÉDICOS <<<{}'.format(cores['azul'], cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosMedicosJSON()
    print('{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
    for medico in baseMedicos.values():
        print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medico['crm'], medico['nome'], medico['email'], medico['especialidade'], medico['clinica']))

def pesquisarMedicoEspecialidade():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'PESQUISAR MÉDICOS POR ESPECIALIDADE', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosMedicosJSON()
    opcao = int(input('Pesquisar por: \n[1] - Cardiologistas \n[2] - Neurologistas \nOpção: '))
    print('\n{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
    if opcao == 1:
        for medico in baseMedicos.values():
            if medico['especialidade'] == 'Cardiologia':
                print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medico['crm'], medico['nome'], medico['email'], medico['especialidade'], medico['clinica']))
    elif opcao == 2:
        for medico in baseMedicos.values():
            if medico['especialidade'] == 'Neurologia':
                print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medico['crm'], medico['nome'], medico['email'], medico['especialidade'], medico['clinica']))
    else: 
        print('{}\nOpção inválida!{}'.format(cores['vermelho'], cores['limpar']))
        

#area do menu de paciente
basePacientes = {}
def carregarPacientes():
    if os.path.exists('basePacientes.json'):
        with open('basePacientes.json', 'r') as arqJson:
            global basePacientes
            basePacientes = json.load(arqJson)
    else:
        with open('basePacientes.json', 'w') as arqJson:
            json.dump(basePacientes, arqJson, indent=4)

def gravarDadosPacientesJSON():
    with open('basePacientes.json', 'w') as arqJson:
        json.dump(basePacientes, arqJson, indent=4)
     
def lerDadosPacientesJSON():
    with open('basePacientes.json', 'r') as arqJson:
        global basePacientes
        basePacientes = json.load(arqJson)
        
def checagemCpf(aux):
    return aux in basePacientes

def cadastroPacientes():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'NOVO PACIENTE', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    carregarPacientes()
    while True:
        while True:
            cpf = str(input('Digite seu CPF: '))
            if checagemCpf(cpf) == True:
                print('{}\nEste CPF já existe no nosso sistema! Digite um CPF válido para continuar \n{}'.format(cores['vermelho'], cores['limpar']))
            else:
                break
        nome = str(input('Nome: '))
        email = str(input('E-mail: '))
        telefone = str(input('Telefone: '))
        endereco = str(input('Cidade: '))       
        basePacientes[cpf] = {'cpf': cpf, 'nome': nome, 'email': email, 'telefone': telefone, 'endereco': endereco}
        print('{}\nCadastro realizado com sucesso! \n{}'.format(cores['verde'], cores['limpar']))
        opcao = int(input('Deseja continuar cadastrando? [1] - Sim | [2] - Não \nOpção: '))
        if opcao != 1:
            break
    gravarDadosPacientesJSON()  

def listagemPacientes():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'LISTAGEM DE PACIENTES', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosPacientesJSON()
    print('{}{:<12} {:<15} {:<15} {:<12} {:<12}{}'.format(cores['amarelo'], 'CPF', 'NOME', 'E-MAIL','TELEFONE' , 'ENDEREÇO', cores['limpar']))
    for paciente in basePacientes.values():
        print('{:<12} {:<15} {:<15} {:<12} {:<12}'.format(paciente['cpf'], paciente['nome'], paciente['email'],paciente['telefone'] , paciente['endereco']))   

def buscarCpf():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'BUSCAR PACIENTE', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosPacientesJSON()
    CPFverif = input('CPF do paciente que deseja buscar: ')
    if checagemCpf(CPFverif):
        for paciente in basePacientes.values():
            if paciente['cpf'] == CPFverif:
                print('\n{}{:<12} {:<15} {:<15} {:<12} {:<12}{}'.format(cores['amarelo'], 'CPF', 'NOME', 'E-MAIL','TELEFONE' , 'ENDEREÇO', cores['limpar']))
                print('{:<12} {:<15} {:<15} {:<12} {:<12}'.format(paciente['cpf'], paciente['nome'], paciente['email'], paciente['telefone'], paciente['endereco']))
    else:
        print('{}\nCPF não encontrado!{}'.format(cores['vermelho'], cores['limpar']))
               
def editarPacientes():  
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EDITAR PACIENTES', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosPacientesJSON()
    CPFverif = input('Digite o CPF do paciente para editar: ')
    if checagemCpf(CPFverif):
        for paciente in basePacientes.values():          
            if paciente['cpf'] == CPFverif:
                print('\n{}{:<12} {:<15} {:<15} {:<12} {:<12}{}'.format(cores['amarelo'], 'CPF', 'NOME', 'E-MAIL','TELEFONE','ENDEREÇO', cores['limpar']))
                print('{:<12} {:<15} {:<15} {:<12} {:<12}'.format(paciente['cpf'], paciente['nome'], paciente['email'], paciente['telefone'] , paciente['endereco']))              
                opcao = int(input('\nDeseja editar? [1]- Sim [2]- Não  '))               
                if opcao == 1 :
                    while True:
                        novoCpf = input('Escreva um novo CPF: ')
                        if checagemCpf(novoCpf):
                            print('{}\nEste CPF já existe no nosso sistema! Digite um CPF válido para continuar\n{}'.format(cores['vermelho'], cores['limpar']))
                        else:
                            break
                    novoNome = input('Escreva um novo nome: ')
                    novoEmail = input('Escreva um novo email: ')
                    novoTelefone = input('Escreva um novo telefone: ')
                    novoEndereco = input('Escreva uma nova cidade: ')
                    paciente = {'cpf': novoCpf, 'nome': novoNome, 'email':novoEmail, 'telefone': novoTelefone, 'endereco': novoEndereco}
                    basePacientes[novoCpf] = paciente
                    del basePacientes[CPFverif]
                    print('{}\nDados editados com sucesso!{}'.format(cores['verde'], cores['limpar']))
                    gravarDadosPacientesJSON()
                    return           
    else:
        print('{}\nCPF não foi encontrado!{}\n'.format(cores['vermelho'], cores['limpar']))  
            
def excluirPaciente():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EXCLUIR PACIENTE', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosPacientesJSON()
    CPFverif = input('Digite o CPF do paciente para excluir: ')
    if checagemCpf(CPFverif):
        for paciente in basePacientes.values():   
            if paciente['cpf'] == CPFverif:
                print('\n{}{:<12} {:<15} {:<15} {:<12} {:<12}{}'.format(cores['amarelo'], 'CPF', 'NOME', 'E-MAIL','TELEFONE','ENDEREÇO', cores['limpar']))
                print('{:<12} {:<15} {:<15} {:<12} {:<12}'.format(paciente['cpf'], paciente['nome'], paciente['email'], paciente['telefone'] , paciente['endereco']))  
                opcao = int(input('\nDeseja excluir? [1] - Sim [2] - Não '))
                if opcao == 1:
                    del basePacientes[CPFverif] 
                    print('{}\nPaciente excluído com sucesso!{}'.format(cores['verde'], cores['limpar']))
                    gravarDadosPacientesJSON()
                    return
    else:
        print('{}\nCPF não encontrado!{}'.format(cores['vermelho'], cores['limpar']))
        

#area do menu de marcação de consulta
baseConsultas = {}

def carregarConsultas():
    if os.path.exists('baseConsultas.json'):
        with open('baseConsultas.json', 'r') as arqJson:
            global baseConsultas
            baseConsultas = json.load(arqJson)
    else:
        with open('baseConsultas.json', 'w') as arqJson:
            json.dump(baseConsultas, arqJson, indent=4)

def gravarDadosConsultasJSON():
    with open('baseConsultas.json', 'w') as arqJson:
        json.dump(baseConsultas, arqJson, indent=4)
     
def lerDadosConsultasJSON():
    with open('baseConsultas.json', 'r') as arqJson:
        global baseConsultas
        baseConsultas = json.load(arqJson)

def checagemCOD(aux):
    return aux in baseConsultas

def checagemConsulta(med, dat):
    for consulta in baseConsultas.values():
        if med == consulta['medico'] and dat == consulta['data']:
            return True

def checagemMedico(med):
    for consulta in baseConsultas.values():
        if med in consulta.values():
            return True

def checagemRetorno(pac, med):
    for consulta in baseConsultas.values():
        if pac == consulta['paciente'] and med == consulta['medico']:
            return True 

def marcarConsulta():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'NOVA CONSULTA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    carregarConsultas()
    lerDadosPacientesJSON()
    lerDadosMedicosJSON()
    while True:
        while True:
            codigo = str(input('Digite seu código: '))
            if checagemCOD(codigo) == True:
                print('{}\nEste código já existe no nosso sistema! Digite um novo código válido para continuar{}\n'.format(cores['vermelho'], cores['limpar']))
            else:
                break
        while True:
            paciente = []
            CPFverif = input('Seu CPF: ')
            if checagemCpf(CPFverif):
                for pacient in basePacientes.values():          
                    if pacient['cpf'] == CPFverif:   
                        print('\n','-'*66)  
                        print('{}{:<12} {:<15} {:<15} {:<12} {:<12}{}'.format(cores['amarelo'], 'CPF', 'NOME', 'E-MAIL','TELEFONE','ENDEREÇO', cores['limpar']))
                        print('{:<12} {:<15} {:<15} {:<12} {:<12}'.format(pacient['cpf'], pacient['nome'], pacient['email'], pacient['telefone'] , pacient['endereco'])) 
                        print('-'*66)
                        opcao = int(input('\nConfirme seus dados: [1]- Sim, sou eu! | [2]- Não, não sou eu! '))
                        if opcao == 1:
                            paciente.append(pacient['cpf'])
                            paciente.append(pacient['nome'])
                if opcao == 1:
                    break
                else:
                    print('{}\nPesquise novamente...{}'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5)
            else:
                print('{}\nCPF não encontrado!\n{}'.format(cores['vermelho'], cores['limpar']))
        while True:
            CRMverif = input('CRM do seu médico: ')
            if checagemCrm(CRMverif):
                for medic in baseMedicos.values():
                    if medic['crm'] == CRMverif:
                        print('\n','-'*66)
                        print('{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
                        print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medic['crm'], medic['nome'], medic['email'], medic['especialidade'], medic['clinica']))
                        print('-'*66)
                        opcao = int(input('\nConfirme os dados do seu médico: [1] - Sim, este é o meu! | [2] - Não, este não é o meu! '))
                        if opcao == 1:
                            medico = medic['nome']
                if opcao == 1:
                    break
                else:
                    print('{}\nRepita o processo por favor...{}\n'.format(cores['amarelo'], cores['limpar']))
                    sleep(1.5)    
            else:
                print('{}\nCRM não encontrado!{}\n'.format(cores['vermelho'], cores['limpar']))
        if checagemMedico(medico):
            print('{}\nDr. {} já tem consultas marcadas para este(s) horário(s):\n{}'.format(cores['azul'], medico, cores['limpar']))
            for consulta in baseConsultas.values():
                if medico == consulta['medico']:
                    print('{}{}{}'.format(cores['azul'], consulta['data'], cores['limpar']))
        while True:
            try:
                data = input('\nInforme a data e a hora da consulta exatamente como mostra o exemplo (ex: 11/05/2022 17:00): ')               
                dataForm = datetime.strptime(data, '%d/%m/%Y %H:%M')
                break
            except ValueError:
                print('{}\nData em formato inválido. Tente novamente {}\n'.format(cores['vermelho'], cores['limpar']))
        if checagemConsulta(medico, data) == True:
            print('{}\nSeu médico já tem uma consulta para esse horário \nRepita o processo e tente com outra data e horário por favor {}\n'.format(cores['vermelho'], cores['limpar']))
            continue
        #a consulta é considerada um retorno quando um paciente marca mais de uma consulta com o mesmo médico
        print('{}Verificando se a consulta é um retorno...{}'.format(cores['amarelo'], cores['limpar']))
        sleep(1.5)
        if checagemRetorno(paciente, medico):
            retorno = 'Sim'
            print('Retorno? {}{}{}'.format(cores['azul'], retorno, cores['limpar']))
        else:
            retorno = 'Não'
            print('Retorno? {}{}{}'.format(cores['azul'], retorno, cores['limpar']))
        observacao = input('\nDeseja adicionar alguma observação? Se não, apenas aperte ENTER: ')
        baseConsultas[codigo] = {'codigo': codigo, 'paciente': paciente, 'medico': medico, 'data': data, 'retorno': retorno, 'observacao': observacao}
        gravarDadosConsultasJSON()
        print('{}\nConsulta marcada com sucesso!{}\n'.format(cores['verde'], cores['limpar']))
        opcao = int(input('Realizar mais um cadastro? [1] - Sim | [2] - Não '))
        if opcao != 1:
            break
       
def buscarConsultaPaciente():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'BUSCAR CONSULTA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosConsultasJSON()
    CPFverif = input('Seu CPF: ')
    print('\n{}{:<10} {:<23} {:<15} {:<20} {:<10} {}{}'.format(cores['amarelo'], 'CÓDIGO', 'PACIENTE', 'MÉDICO','DATA', 'RETORNO', 'OBSERVAÇÃO', cores['limpar']))
    for consulta in baseConsultas.values():
        if CPFverif in consulta['paciente'][0]: 
           print('{:<10} {} - {:<15} {:<15} {:<20} {:<10} {}'.format(consulta['codigo'], consulta['paciente'][0], consulta['paciente'][1], consulta['medico'], consulta['data'], consulta['retorno'], consulta['observacao']))
           
def editarConsulta():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EDITAR CONSULTA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosConsultasJSON()
    lerDadosMedicosJSON()
    codVerif = input('Informe o código da consulta: ')
    if checagemCOD(codVerif):
        for consulta in baseConsultas.values():
            if consulta['codigo'] == codVerif:
                print('\n{}{:<10} {:<23} {:<15} {:<20} {:<10} {}{}'.format(cores['amarelo'], 'CÓDIGO', 'PACIENTE', 'MÉDICO','DATA', 'RETORNO', 'OBSERVAÇÃO', cores['limpar']))
                print('{:<10} {} - {:<15} {:<15} {:<20} {:<10} {}'.format(consulta['codigo'], consulta['paciente'][0], consulta['paciente'][1], consulta['medico'], consulta['data'], consulta['retorno'], consulta['observacao']))
                opcao = int(input('\nDeseja realmente editar esta consulta? [1] - Sim | [2] - Não '))
                if opcao == 1:
                    while True:
                        while True:
                            crmVerif = input('CRM do seu novo médico: ')
                            for medic in baseMedicos.values():
                                if medic['crm'] == crmVerif:
                                    print()
                                    print('-'*68)
                                    print('{}{:<12} {:<15} {:<15} {:<15} {:<12}{}'.format(cores['amarelo'], 'CRM', 'NOME', 'E-MAIL', 'ESPECIALIDADE', 'CLÍNICA', cores['limpar']))
                                    print('{:<12} {:<15} {:<15} {:<15} {:<12}'.format(medic['crm'], medic['nome'], medic['email'], medic['especialidade'], medic['clinica']))
                                    print('-'*68)
                                    print()
                                    opcao = int(input('Deseja substituir seu médico por este? [1] - Sim | [2] - Não '))
                                    if opcao == 1:
                                        novoMedico = medic['nome']
                            if opcao == 1:
                                break
                            else:
                                print('{}\nRepita o processo por favor...{}\n'.format(cores['amarelo'], cores['limpar']))
                                sleep(1.5)
                        if checagemMedico(novoMedico):
                            print('{}\nDr. {} já tem consultas marcadas para este(s) horário(s):\n{}'.format(cores['azul'], novoMedico, cores['limpar']))
                            for consulta in baseConsultas.values():
                                if novoMedico == consulta['medico']:
                                    print('{}{}{}'.format(cores['azul'], consulta['data'], cores['limpar']))
                        while True:
                            try:
                                novaData = input('\nInforme a data e a hora da consulta exatamente como mostra o exemplo (ex: 11/05/2022 17:00): ')               
                                dataForm = datetime.strptime(novaData, '%d/%m/%Y %H:%M')
                                break
                            except ValueError:
                                print('{}\nData em formato inválido. Tente novamente {}\n'.format(cores['vermelho'], cores['limpar']))
                        if checagemConsulta(novoMedico, novaData):
                            print('{}\nSeu médico já tem uma consulta para esse horário. \nRepita o processo e tente com outra data e horário por favor {}\n'.format(cores['vermelho'], cores['limpar']))
                            continue
                        print('{}Verificando se a consulta é um retorno...{}'.format(cores['azul'], cores['limpar']))
                        sleep(1.5)
                        if checagemRetorno(baseConsultas[codVerif]['paciente'], novoMedico):
                            novoRetorno = 'Sim'
                            print('Retorno? {}{}{}'.format(cores['azul'], novoRetorno, cores['limpar']))
                        else:
                            novoRetorno = 'Não'
                            print('Retorno? {}{}{}'.format(cores['azul'], novoRetorno, cores['limpar']))
                        novaObservacao = input('\nDeixe uma observação, caso tenha alguma. Se não tiver apenas aperte ENTER: ')
                        baseConsultas[codVerif] = {'codigo': codVerif, 'paciente': consulta['paciente'], 'medico': novoMedico, 'data': novaData, 'retorno': novoRetorno, 'observacao': novaObservacao}
                        print('{}\nConsulta editada com sucesso!{}'.format(cores['verde'], cores['limpar']))
                        gravarDadosConsultasJSON()
                        return
                        
    else:
        print('{}\nCódigo de consulta não encontrado!{}'.format(cores['vermelho'], cores['limpar']))
        
def excluirConsulta():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'EXCLUIR CONSULTA', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosConsultasJSON()
    codVerif = input('Informe o código da consulta que deseja excluir: ')
    if checagemCOD(codVerif):
        for consulta in baseConsultas.values():
            if consulta['codigo'] == codVerif:
                print('\n{}{:<10} {:<23} {:<15} {:<20} {:<10} {}{}'.format(cores['amarelo'], 'CÓDIGO', 'PACIENTE', 'MÉDICO','DATA', 'RETORNO', 'OBSERVAÇÃO', cores['limpar']))
                print('{:<10} {} - {:<15} {:<15} {:<20} {:<10} {}'.format(consulta['codigo'], consulta['paciente'][0], consulta['paciente'][1], consulta['medico'], consulta['data'], consulta['retorno'], consulta['observacao']))
                opcao = int(input('\nQuer realmente excluir esta consulta? [1] - Sim | [2] - Não '))
                if opcao == 1:
                    del baseConsultas[codVerif]
                    gravarDadosConsultasJSON()
                    print('{}\nConsulta excluída com sucesso!{}'.format(cores['verde'], cores['limpar']))
                    return
                else:
                    print('{}\nRetornando para o menu anterior...{}'.format(cores['amarelo'], cores['limpar']))
    else:
        print('{}\nNenhuma consulta com este código foi encontrado!{}'.format(cores['vermelho'], cores['limpar']))
        
def listarConsultas():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'LISTAR CONSULTAS', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosConsultasJSON()
    print('{}{:<10} {:<23} {:<15} {:<20} {:<10} {}{}'.format(cores['amarelo'], 'CÓDIGO', 'PACIENTE', 'MÉDICO','DATA', 'RETORNO', 'OBSERVAÇÃO', cores['limpar']))
    for consulta in baseConsultas.values():
        print('{:<10} {} - {:<15} {:<15} {:<20} {:<10} {}'.format(consulta['codigo'], consulta['paciente'][0], consulta['paciente'][1], consulta['medico'], consulta['data'], consulta['retorno'], consulta['observacao']))
        
def listarConsultasRetorno():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'CONSULTAS RETORNO', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosConsultasJSON()
    if baseConsultas != '':
        print('{}{:<10} {:<23} {:<15} {:<20} {:<10} {}{}'.format(cores['amarelo'], 'CÓDIGO', 'PACIENTE', 'MÉDICO','DATA', 'RETORNO', 'OBSERVAÇÃO', cores['limpar']))
        for consulta in baseConsultas.values():
            if consulta['retorno'] == 'Sim':
                print('{:<10} {} - {:<15} {:<15} {:<20} {:<10} {}'.format(consulta['codigo'], consulta['paciente'][0], consulta['paciente'][1], consulta['medico'], consulta['data'], consulta['retorno'], consulta['observacao']))
    else:
        print('{}\nNenhuma consulta de retorno foi encontrada!{}'.format(cores['vermelho'], cores['limpar']))

def formData(aux):
    dataForm = datetime.strptime(aux, '%d/%m/%Y %H:%M')
    return dataForm

def listarConsultasData():
    print()
    print('{} >>> {:^80} <<<{}'.format(cores['azul'], 'LISTAR CONSULTAS POR INTERVALO DE DATAS', cores['limpar']))
    print('{} {} {}\n'.format(cores['azul'], '='*88, cores['limpar']))
    lerDadosConsultasJSON()
    print('Para realizar a listagem por intervalo de datas, insira a data de início e de final para realizarmos a análise.')
    while True:
        try:
            dataInicial = input('\nInforme a data {}inicial{} da forma que está no exemplo (ex: 11/05/2022 17:00): '.format(cores['amarelo'], cores['limpar']))
            dataInicialForm = datetime.strptime(dataInicial, '%d/%m/%Y %H:%M')
            break
        except ValueError:
            print('{}\nData informada em um formato inválido. Tente novamente!{}\n'.format(cores['vermelho'], cores['limpar']))
    while True:
        try:
            dataFinal = input('\nInforme a data {}final{} da forma que está no exemplo (ex: 11/05/2022 17:00): '.format(cores['amarelo'], cores['limpar']))
            dataFinalForm = datetime.strptime(dataFinal, '%d/%m/%Y %H:%M')
            break
        except ValueError:
            print('{}\nData informada em um formato inválido. Tente novamente!{}\n'.format(cores['vermelho'], cores['limpar'])) 
    if baseConsultas != '':
        print('\n{}{:<10} {:<23} {:<15} {:<20} {:<10} {}{}'.format(cores['amarelo'], 'CÓDIGO', 'PACIENTE', 'MÉDICO','DATA', 'RETORNO', 'OBSERVAÇÃO', cores['limpar']))
        for consulta in baseConsultas.values():
            dataConForm = formData(consulta['data'])
            if dataConForm >= dataInicialForm and dataConForm <= dataFinalForm:
                print('{:<10} {} - {:<15} {:<15} {:<20} {:<10} {}'.format(consulta['codigo'], consulta['paciente'][0], consulta['paciente'][1], consulta['medico'], consulta['data'], consulta['retorno'], consulta['observacao']))
    else:
        print('{}\nNão há nenhuma consulta marcada entre este intervalo!{}'.format(cores['vermelho'], cores['limpar']))    