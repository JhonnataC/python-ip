algoritmo "Questão 02"
var
   c, mai, val: inteiro
inicio
      mai <- 0
      c <- 0
      Enquanto (c < 10) faca
               Escreva("Digite um valor: ")
               Leia(val)
               Se (val > 100) entao
                  mai <- mai + 1
               fimse
               c <- c + 1
      fimenquanto
      Escreva("Quantidade de valores maiores que 100: ", mai)
fimalgoritmo