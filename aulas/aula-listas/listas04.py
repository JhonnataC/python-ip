#append() adiciona um valor no fim da lista
l1 = [1, 2, 3, 4]
print(l1)
l1.append(22)
print(l1)
print(20*'=')

x = l1.pop(0) #pop() remove um indice e o guarda pra retornar
print(l1)
print('Deletado: {}'.format(x))
print(20*'=')

l1 = [1, 2, 3, 4, 5] #insert() insere um obj no indice indicado
l1.insert(3, 99)
print(l1)
print(20*'=')

l1 = [1, 2, 3, 4, 5] #remove() remove a primeira ocorrencia de obj na lista
l1.remove(4)
print(l1)
print(20*'=')

l1 = [1, 2, 3, 4, 5] #index() retorna o indice em que o obj inidicado aparece pela primeira vez
print(l1.index(4))

