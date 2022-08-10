no1 = float(input('1° nota: '))
no2 = float(input('2° bota: '))
med = (no1 + no2) / 2

if med >=0 and med <= 10:
    print('Média: {:.2f}'.format(med))

if med == 10: 
    print('Aluno aprovado com distinção!')
elif med >= 7 and med < 10: 
    print('Aluno aprovado!')
elif med < 7 and med >= 0:
    print('Aluno reprovado!')
else: 
    print('Valores inválidos, repita o processo.')
    