quant = int(input('De quantos alunos deseja calcular a média? '))

for i in range(1,quant+1):
    n1 = float(input('1° nota: '))
    n2 = float(input('2° nota: '))
    med = (n1+n2)/2
    print('Média: {:.2f}'.format(med))
    if med == 10:
        print('Aprovado com distinção!')
    elif med < 10 and med >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')