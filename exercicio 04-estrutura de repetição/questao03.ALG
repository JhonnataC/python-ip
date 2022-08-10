algoritmo "Questão 03"
var
   c, val, som, prod: inteiro
inicio
      c <- 0
      som <- 0
      prod <- 1
      Enquanto (c < 20) faca
               Escreva ("Digite um valor: ")
               Leia(val)
               som <- som + val
               prod <- prod * val
               c <- c + 1
      fimenquanto
      EscrevaL("Resultados")
      EscrevaL("Soma dos valores: ", som)
      Escreva("Produto dos valores: ", prod)
fimalgoritmo