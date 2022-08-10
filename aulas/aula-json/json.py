import json


alunosCadastrados = {}
 
dadosAluno = {'mat': 111, 'nome': 'Jhonnata', 'nota': 9}
alunosCadastrados[111] = dadosAluno
dadosAluno = {'mat': 222, 'nome': 'Cláudia', 'nota': 9.5}
alunosCadastrados[222] = dadosAluno

with open('alunosCadastrados.json', 'w') as arqJson:
    json.dump(alunosCadastrados, arqJson, indent=4)