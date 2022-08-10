lada = float(input('Digite o primeiro lado: '))
ladb = float(input('Digite o segundo lado: '))
ladc = float(input('Digite o terceiro lado: '))
a = lada
b = ladb
c = ladc
if (b-c)  <abs(a)  <  (b+c)  and  (a-c) <  abs(b) < (a+c)  and  (a-b) < abs(c) < (a+b) :
    print(True , 'Forma um triângulo')

else:
    print(False , 'Não forma um triângulo')
    