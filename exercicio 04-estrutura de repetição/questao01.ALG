algoritmo "Questão 02"
var
   c, val, mai: inteiro
inicio
      mai <- 0
      c <- 0
      Enquanto (c < 10) faca
               Escreva("Digite um valor: ")
               Leia(val)
               Se (val > 100) entao
                  mai <- mai + 1
               fimse
      fimenquanto
      Escreva("Quantidade de valores maiores que 100: ", mai)
fimalgoritmo