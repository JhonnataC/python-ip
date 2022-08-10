mat = [[1, 2, 3, 4], [5, 6, 7, 8]]

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], ' ', end = '')
    print()
    

matriz = [1] * 4
print(matriz)
print(15*'=')
matriz1 = [matriz] * 4
print(matriz1)
print(15*'=')
for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        print(matriz1[i][j], ' ', end = '')
    print()