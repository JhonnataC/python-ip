matriz = []
nLin = int(input('Número de linhas: '))
nCol = int(input('Número de colunas: '))

for i in range(nLin):
    linha = []
    for j in range(nCol):
        val = input('Valor: ')
        linha.append(val)
    matriz.append(linha)
    print(5*'=')

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], ' ', end = '')
    print()