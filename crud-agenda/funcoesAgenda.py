from time import sleep

listaDeContatos = []

def adicionarContato():
    dados = []
    print()
    print(24*'=')
    print('-=-ADICIONAR CONTATO-=-')
    print(24*'=')
    print()    
    while True:
        nome = str(input('Nome: '))       
        while True:
            check = 0
            num = int(input('Número (sem espaços): '))
            check = checkNumero(num)
            if check != 0:
                print('Este número já pertence aos seus contatos!')
            else:
                break
        cidade = str(input('Cidade: '))
        dados = [nome, num, cidade]
        listaDeContatos.append(dados)
        res = str(input('Deseja adicionar mais um contato? \n[S] - Sim | [N] - Não ')).upper()
        if res == 'N':
            break
       
def checkNumero(aux):
    b = 0
    for i in range(0, len(listaDeContatos)):
        if listaDeContatos[i][1] == aux:
            b += 1
    return b

def verContatos():
    print()
    print(19*'=')
    print('-=-SEUS CONTATOS-=-')
    print(19*'=')
    print()
    print('{:<18}  {:<12}  {:<15}'.format('NOME', 'NÚMERO', 'CIDADE'))
    for i in range(0, len(listaDeContatos)):
        print('{:<18}  {:<12}  {:<15}'.format(listaDeContatos[i][0], listaDeContatos[i][1], listaDeContatos[i][2]))
        
def pesquisarContato():
    print()
    print(15*'=')
    print('-=-PESQUISAR-=-')
    print(15*'=')
    print()
    print('Desejar pesquisar por: \n[1] - Nome \n[2] - Número \n[3] - Cidade')
    res = int(input('Opção: '))
    contato = []
    contEncontrados = []
    if res == 1:
        nomePesquisado = str(input('Digite o nome: '))
        for i, contato in enumerate(listaDeContatos):
            if contato[0].upper() == nomePesquisado.upper():
                contEncontrados.append(listaDeContatos[i])
    elif res == 2:
        numPesquisado = int(input('Digite o número: '))
        for i, contato in enumerate(listaDeContatos):
            if contato[1] == numPesquisado:
                contEncontrados.append(listaDeContatos[i])
    elif res == 3:
        cidPesquisada = str(input('Digite a cidade: '))
        for i, contato in enumerate(listaDeContatos):
            if contato[2].upper() == cidPesquisada.upper():
                contEncontrados.append(listaDeContatos[i])  
    print('Pesquisando...')
    sleep(2)     
    print('Contato(s) encontrado(s):')
    if contEncontrados != []:
        for i in range(0,len(contEncontrados)):
            print('{:<18}  {:<12}  {:<15}'.format(contEncontrados[i][0], contEncontrados[i][1], contEncontrados[i][2]))
    else:
        print('Nenhum contato encontrado!')
        
def editarContato():
    print()
    print(20*'=')
    print('-=-EDITAR CONTATO-=-')
    print(20*'=')
    print()   
    contEdit = int(input('Número do contato que deseja editar: '))
    contato = []
    for i, contato in enumerate(listaDeContatos):
        if contato[1] == contEdit:
            print(contato)
            res = str(input('Deseja realmente editar o contato de {}? \n[S] - Sim | [N] - Não '.format(contato[0]))).upper()
            if res == 'S':
                op = int(input('[1] - Editar nome \n[2] - Editar número \n[3] - Editar cidade \nOpção: '))
                if op == 1:
                    listaDeContatos[i][0] = str(input('Novo nome: '))
                elif op == 2:
                    while True:
                        check = 0
                        novoNum = int(input('Novo número (sem espaços): '))
                        check = checkNumero(novoNum)
                        if check != 0:
                            print('Este número já pertence aos seus contatos!')
                        else:
                            listaDeContatos[i][1] = novoNum
                            break
                elif op == 3:
                    listaDeContatos[i][2] = str(input('Nova cidade: '))
                print('Contato editado com sucesso!')
            else:
                print('Retornando ao menu...')

def excluirContato():
    print()
    print(21*'=')
    print('-=-EXCLUIR CONTATO-=-')
    print(21*'=')
    print()
    contDel = int(input('Digite o número do contato que deseja deletar: '))
    contato = []
    for i, contato in enumerate(listaDeContatos):
        if contato[1] == contDel:
            print(contato)
            res = str(input('Deseja realmente deletar o contato de {}? [S] - Sim | [N] - Não '.format(contato[0]))).upper()
            if res == 'S':
                listaDeContatos.pop(i)
                print('Contato deletado com sucesso!')
            