cm = float(input('Quantos centímetros você quer converter? '))
yard = cm // 91.44
foot = cm // 30.48
inche = cm // 2.54
print('Em {} cm, há: '.format(cm))

if yard == 0:
    print()
elif yard == 1:
    print('{} jarda'.format(yard))
else:
    print('{} jardas'.format(yard))

if foot == 0:
    print()
elif foot == 1: 
    print('{} pé'.format(foot))
else:
    print('{} pés'.format(foot))

if inche == 0:
    print()
elif inche == 1:
    print('{} polegada'.format(inche))
else:
    print('{} polegadas'.format(inche))