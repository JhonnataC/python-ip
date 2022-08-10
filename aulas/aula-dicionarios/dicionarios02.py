ramais = {'Carlos':2066, 'Maria': 2088, 'Renato': 2190}

print(ramais)
print(20*'=')

#Operadores

#in = verificar se uma chave existe no dicionario
print('Carlos' in ramais)

#del = excluir um item do dicionario informando a chave 
del ramais['Maria']
print(ramais)

ramais = {'Carlos':2066, 'Maria': 2088, 'Renato': 2190}

#keys() = obtem as chaves do dicionario
print(ramais.keys())

#values() = obtem os valores do dicionario
print(ramais.values())

#len() = retorna o tamanho do dicionario
print(len(ramais))
print(ramais)

#fazendo um for
for codigo, valor in ramais.items():
    print('Chave: {}  Valor: {}'.format(codigo, valor))