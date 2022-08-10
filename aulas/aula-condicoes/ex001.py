res = str(input('Você quer calcular? S/N '))
if (res == 'S') or (res == 's'):
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    som = n1 + n2
    print('A soma é: {}'.format(som))
else:
    print('Fim do programa')
