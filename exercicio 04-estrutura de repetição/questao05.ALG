algoritmo "Questão 05"
var
   peso, med, som, mai: real
   c: inteiro
inicio
      mai <- 0
      c <- 0
      Enquanto (peso >= 0) faca
               Escreva("O peso (kg): ")
               Leia(peso)
               Se (peso > 60) entao
                  som <- som + peso
                  c <- c + 1
               fimse
               Se (peso > mai) entao
                  mai <- peso
               fimse
      fimenquanto
      med <- som / c
      EscrevaL("O maior peso foi: ", mai, " Kg.")
      Escreva("E a média dos pesos acima de 60kg, foi igual a: ", med:5:2, "Kg.")
fimalgoritmo