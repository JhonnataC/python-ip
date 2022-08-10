num = int(input('Até que número deseja fazer a contagem? '))
npar = 0
spar = 0 
nimpar = 0
simpar = 0

for i in range(1, num+1):
    if i%2 == 0:
        npar += 1
        spar = spar + i
    else:
        nimpar += 1
        simpar = simpar + i

print('Quantidade de números pares entre 1 e {}: {}. Soma deles: {}'.format(num, npar, spar))
print('Quantidade de números ímpares entre 1 e {}: {}. Soma deles: {}'.format(num, nimpar, simpar))
