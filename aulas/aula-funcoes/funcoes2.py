def quadrado(x,y = 2):
    quad = pow(x,y)
    return quad

num = int(input('Digite o numero que deseja elevar ao quadrado: '))
print('{} elevado ao quadrado é igual a: {}'.format(num, quadrado(num)))