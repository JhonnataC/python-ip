algoritmo "Quest?o 03"
var
   valorV, salM, com: real
inicio
    Escreva("Informe o valor total das suas vendas no m?s: R$ ")
    Leia(valorV)
    com <- (valorV*25/100)
    salM <- 800 + com
    EscrevaL("=============================")
    EscrevaL("Comiss?o do m?s: R$ ", com:5:2)
    EscrevaL("Sal?rio total do m?s: R$ ", salM:5:2)
fimalgoritmo