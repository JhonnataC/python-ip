algoritmo "Questão 05"
var
   ind: real
inicio
    Escreva("Informe o índice de poluição: ")
    Leia(ind)
    Se (ind < 35) e (ind > 0) entao
       Escreva("Agradável")
    senao
       Se (ind >= 35) e (ind < 60) entao
          Escreva("Desagradável")
       senao
          Escreva("Perigoso")
       fimse
    fimse
fimalgoritmo