per = float(input('Por favor, informe o seu percentual: '))

if per <= 100 and per >= 93.33:
    nota = 'A'
elif per < 93.33 and per >= 90:
    nota = 'A-'
elif per < 90 and per >= 86.67:
    nota = 'B+'
elif per < 86.67 and per >= 83.33:
    nota = 'B'
elif per < 83.33 and per >= 80:
    nota = 'B-'
elif per < 80 and per >= 76.67:
    nota = 'C+'
elif per < 76.67 and per >= 73.33:
    nota = 'C'
elif per < 73.33 and per >= 70:
    nota = 'C-'
elif per < 70 and per >= 66.67:
    nota = 'D+'
elif per < 66.67 and per >= 63.33:
    nota = 'D'
elif per < 63.33 and per >= 60: 
    nota = 'D-'
else: 
    nota = 'F'

print('Você ganhou um {}.'.format(nota))