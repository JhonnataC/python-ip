algoritmo "Questão 03"
var
   valorV, salM, com: real
inicio
    Escreva("Informe o valor total das suas vendas no mês: R$ ")
    Leia(valorV)
    com <- (valorV*25/100)
    salM <- 800 + com
    EscrevaL("=============================")
    EscrevaL("Comissão do mês: R$ ", com:5:2)
    EscrevaL("Salário total do mês: R$ ", salM:5:2)
fimalgoritmo