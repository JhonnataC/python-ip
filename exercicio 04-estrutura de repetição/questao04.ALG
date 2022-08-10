algoritmo "Questão 04"
var
   c, ap, re: inteiro
   n1, n2, m: real
inicio
      c <- 0
      ap <- 0
      re <- 0
      Enquanto (c < 50) faca
               Escreva("1° nota: ")
               Leia(n1)
               Escreva("2° nota: ")
               Leia(n2)
               m <- (n1 + n2) / 2
               EscrevaL("Média: ", m)
               Se (m >= 7) entao
                  ap <- ap + 1
                  Escreva("Aprovado")
               senao
                  re <- re + 1
                  Escreva("Reprovado")
               fimse
               c <- c + 1
               limpatela
      fimenquanto
      EscrevaL("Quantidade de aprovados: ", ap)
      Escreva("Quantidade de reprovados: ", re)
fimalgoritmo