algoritmo "Questão 04"
var
   copos, pizza, adi, pes: inteiro
   conta, gor, tpagar, vpes: real
inicio
    Escreva("Quantidade de copos de refrigerante comprados: ")
    Leia(copos)
    Escreva("Quantidade de pizzas: ")
    Leia(pizza)
    Escreva("Quantidade de adicionais escolhidos: ")
    Leia(adi)
    conta <- (copos * 0.80) + (pizza * 10) + (adi * 1.50)
    gor <- (conta*10/100)
    tpagar <- conta + gor
    EscrevaL("============================")
    EscrevaL("Valor da conta: R$ ", conta:5:2)
    EscrevaL("Gorjeta do garçom: R$ ", gor:5:2)
    EscrevaL("Total à pagar: R$", tpagar:5:2)
    EscrevaL("============================")
    Escreva("Deseja dividir para quantas pessoas? ")
    Leia(pes)
    vpes <- tpagar / pes
    Escreva("Cada um irá pagar: R$ ", vpes:5:2)
fimalgoritmo