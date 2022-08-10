num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('[1] Somar \n[2] Subtrair \n[3] Multiplicar \n[4] Dividir \n[5] Sair')
res = int(input('Informe a opção: '))

if (res == 1): 
    r = (num1 + num2)
elif (res == 2):
    r = (num1 - num2)
elif (res == 3):
    r = (num1 * num2)
elif (res == 4):
    r = (num1 / num2)
elif (res == 5):
    print('Aplicação finalizada')
else:
    print('Opção inválida')

if (res > 0) and (res < 5):
    print('O resultado é: {}'.format(r))

