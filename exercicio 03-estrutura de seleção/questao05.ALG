algoritmo "Quest?o 05"
var
   ind: real
inicio
    Escreva("Informe o ?ndice de polui??o: ")
    Leia(ind)
    Se (ind < 35) e (ind > 0) entao
       Escreva("Agrad?vel")
    senao
       Se (ind >= 35) e (ind < 60) entao
          Escreva("Desagrad?vel")
       senao
          Escreva("Perigoso")
       fimse
    fimse
fimalgoritmo