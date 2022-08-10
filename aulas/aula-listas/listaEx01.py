listaAlunos = []
listaAprovados = []
listaReprovados = []

def menu():
    print('\n'+35*'*')
    print('[1] - Cadastrar aluno')
    print('[2] - Listar alunos')
    print('[3] - Calcular média geral da turma')
    print('[4] - Listar aprovados')
    print('[5] - Listas reprovados')
    print('[6] - Sair')
    op = int(input('Digite uma das opções: '))
    print('')
    return op

def cadastrarAluno():
    print('====CADASTRO DE ALUNO====')
    
    while True:
        while True:
            chec = True
            matricula = int(input('Digite a matricula: '))
            chec = checkMatricula(matricula)
            if chec != 0:
                print('Matricula já cadastrada.')
            else:
                break
            
        nome = str(input('Digite o nome: '))
        n1 = float(input('1° nota: '))
        n2 = float(input('2° nota: '))
        media = (n1 + n2)/2
        aluno = [matricula, nome, media]
        listaAlunos.append(aluno)
        re = int(input('Deseja continuar cadastrando? [1] - Sim | [2] - Não '))
        if re != 1:     
            break
        
def checkMatricula(a):
    b = 0
    for i in range(0, len(listaAlunos)):
        if a == listaAlunos[i][0]:
            b += 1
    return b 
    
            
def listarAluno():
    print('====Listar Alunos====')
    print('Matrícula | Nome | Média')
    for i in range(0, len(listaAlunos)):
        print('   {}    | {} |  {}'.format(listaAlunos[i][0], listaAlunos[i][1], listaAlunos[i][2]))    

def calcuMedia():
    soma = 0
    print('====CALCULAR MÉDIA GERAL====')
    
    for i in range(0, len(listaAlunos)):
        soma += listaAlunos[i][2]
        
    mediaG = soma/len(listaAlunos)
    print('Média geral: {:.2f}'.format(mediaG))
    
def listarAprovados():
    print('====LISTA DE APROVADOS====')
    
    for i in range(0, len(listaAlunos)):
        if listaAlunos[i][2] >= 7 and listaAlunos[i][2] <= 10:
            listaAprovados.append(listaAlunos[i][1])
    print('Aprovados: ')
    for i in range(0, len(listaAprovados)):
        print('{}'.format(listaAprovados[i]))
    
def listarReprovados():
    print('====LISTA DE REPROVADOS====')
    
    for i in range(0, len(listaAlunos)):
        if listaAlunos[i][2] < 7:
            listaReprovados.append(listaAlunos[i][1])
    print('Reprovados:')
    for i in range(0, len(listaReprovados)):
        print('{}'.format(listaReprovados[i]))
    
def main():
    
    while True:
        opMenu = menu()    
        if opMenu == 1:
            cadastrarAluno()
        elif opMenu == 2:
            listarAluno()
        elif opMenu == 3:
            calcuMedia()
        elif opMenu == 4:
            listarAprovados()
        elif opMenu == 5:
            listarReprovados()
        elif opMenu == 6:
            print('Encerrando...')
            break
        else:
            print('Opção inválida')
            
main()