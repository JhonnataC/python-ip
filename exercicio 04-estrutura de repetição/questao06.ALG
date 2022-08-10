algoritmo "Questão 06"
var
   n, c, p, i: inteiro
inicio
    p <- 0
    i <- 1
    c <- 0
    Escreva("Informe quantos termos deseja ver: ")
    Leia(n)
    EscrevaL("==========Pares==========")
    Enquanto (c < n) faca
             p <- p + 2
             EscrevaL(p)
             c <- c + 1
    fimenquanto
    EscrevaL("=========Ímpares=========")
    c <- 0
    Enquanto (c < n) faca
             EscrevaL(i)
             i <- i + 2
             c <- c + 1
    fimenquanto
fimalgoritmo