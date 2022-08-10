def soma(x,y):
    return(x+y)

def main():
    while True:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        s = soma(num1,num2)
        print('A soma é: {}'.format(s))
        r = str(input('Deseja continuar? [S - Sim] [N - Não]'))
        if r.upper() == 'N':
            break
    
main()    