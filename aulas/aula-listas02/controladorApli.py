listaAlunos = []
listaAprovados = []
listaReprovados = []

def cadastrarAluno():
    print('====CADASTRO DE ALUNO====')
    
    while True:
        while True:
            chec = 0
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
    print('Matrícula  |  Nome  |  Média')
    for i in range(0, len(listaAlunos)):
        print('   {}\t{}\t{}'.format(listaAlunos[i][0], listaAlunos[i][1], listaAlunos[i][2]))    

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
        
def removerAluno():
    print('====REMOVER ALUNO====')
    delMat = int(input('Digite a matricula do aluno que deseja deletar: '))  
    aluno = []
    for i, aluno in enumerate(listaAlunos):
        if aluno[0] == delMat:
            op = int(input('Tem certeza que deseja excluir o aluno {}? [1] - Sim | [2] - Não '.format(aluno[1])))
            if op == 1:
                listaAlunos.pop(i)
                print('Aluno deletado com sucesso.')
    print('Aluno não encontrado.')            

def editarAluno():
    print('====EDITAR CADASTRO====')
    editMat = int(input('Matricula do aluno que deseja editar o cadastro: '))
    
    aluno = []
    for i, aluno in enumerate(listaAlunos):
        if aluno[0] == editMat:
            print(aluno)
            op = int(input('Deseja editar o cadastro do aluno {}? [1] - Sim | [2] - Não '.format(aluno[1])))
            if op == 1:
                print('[1] - Editar matricula')
                print('[2] - Editar nome')
                print('[3] - Editar notas')
                op1 = int(input('Opção: '))
                if op1 == 1:   
                    mat = int(input('Nova matricula: '))
                    aluno[0] = mat
                elif op1 == 2:
                    nome = str(input('Nome: '))
                    aluno[1] = nome
                elif op1 == 3:
                    n1 = float(input('1° nota: '))
                    n2 = float(input('2° nota: '))
                    med = (n1 + n2)/2
                    aluno[2] = med
        listaAlunos[i] = aluno 
        print(aluno)
        print('Edição relizada com sucesso.')