alunosCadastrados = {}
 
dadosAluno = {'mat': 111, 'nome': 'Jhonnata', 'nota': 9}
alunosCadastrados[111] = dadosAluno
dadosAluno = {'mat': 222, 'nome': 'Cláudia', 'nota': 9.5}
alunosCadastrados[222] = dadosAluno

f = open('alunosCadastrados.txt', 'w')
for alunos in alunosCadastrados.values():
    f.write('{} {:>15} {:>15} \n'.format(alunos.get('mat'), alunos.get('nome'), alunos.get('nota')))
    
print(f)
f.close()