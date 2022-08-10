print('Por favor, informe os dados abaixo para saber asua porcentagem de aumento e o valor do seu novo salário: ')
nome = str(input('Seu nome: '))
sal = float(input('Seu salário atual: R$ '))

if sal > 0 and sal <= 400:
    por = 15
elif sal > 400 and sal <= 700: 
    por = 12
elif sal > 700 and sal <= 1000:
    por = 10
elif sal > 1000 and sal <= 1800:
    por = 7
elif sal > 1800 and sal <= 2500:
    por = 4
else: 
    por = 0
    
salN = sal + sal*por/100

if sal > 0 and sal <= 2500:
    print('Olá {}! \nSua porcentagem de aumento é de {}% \nSalário antigo: R$ {:.2f} \nSalário novo: R$ {:.2f}'.format(nome, por, sal, salN))
else:
    print('Não temos aumento para a sua faixa de salário!')