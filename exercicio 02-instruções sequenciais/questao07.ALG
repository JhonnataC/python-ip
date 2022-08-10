algoritmo "Questão 07"
var
   custoFab, custoFinal: real
inicio
    Escreva("Custo de fábrica do carro: R$ ")
    Leia(custoFab)
    custoFinal <- custoFab + (custoFab*45/100) + (custoFab*25/100)
    Escreva("Valor para o consumidor: R$ ", custoFinal:8:2)
fimalgoritmo