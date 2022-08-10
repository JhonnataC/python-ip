def questao5():
    somaMulhe = 0
    somaHomem = 0
    somaGrup = 0 
    quantHomem = 0 
    quantMulhe = 0
    
    print('======ANALISANDO PESSOAS======')
    for i in range(1,11):
        sexo = str(input('Informe seu sexo [M]-Masculino [F]-Feminino: '))
        idade = int(input('Informe sua idade: '))
        
        if sexo.upper() == 'F':
            somaMulhe += idade
            somaGrup += idade
            quantMulhe += 1
        elif sexo.upper() == 'M':
            somaHomem += idade
            somaGrup += idade
            quantHomem += 1
            
    medMulhe = somaMulhe/quantMulhe
    medHomem = somaHomem/quantHomem
    medGrupo = somaGrup/10

    print('===Resultados===')
    print('Idade média dos homens: {}'.format(medHomem))
    print('Quantidade de homens: {}'.format(quantHomem))
    print('Idade média das mulheres: {}'.format(medMulhe))
    print('Quantidade de mulheres: {}'.format(quantMulhe))
    print('Idade média do grupo: {}'.format(medGrupo))
    
