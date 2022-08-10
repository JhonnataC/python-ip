def questao6():
    maiorSal = 0
    menorSal = 0
    nomeMaior = 0
    nomeMenor = 0
    somaSal = 0
    interacao = 1
    print('======MAIOR E MENOR SALÁRIO======')
    quantEmp = int(input('Quantidade de empregados que deseja cadastrar: '))
    
    for i in range(1, quantEmp+1):
        matri = int(input('Matricula: '))
        nome = str(input('Nome: '))
        sal = float(input('Salário: '))
        if interacao == 1:
            maiorSal = sal
            nomeMaior = nome
            menorSal = sal
            nomeMenor = nome
            interacao += 1
        if sal < menorSal:
            menorSal = sal
            nomeMenor = nome
        if sal > maiorSal:
            maiorSal = sal 
            nomeMaior = nome
        somaSal += sal

    medSal = somaSal/quantEmp
    print('Média salarial: {}'.format(medSal))
    print('Maior salário: R$ {} Nome do empregado com maior salário: {}'.format(maiorSal, nomeMaior))
    print('Menor salário: R$ {} Nome do empregado com menor salário: {}'.format(menorSal, nomeMenor))

