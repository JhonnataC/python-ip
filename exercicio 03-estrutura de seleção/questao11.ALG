algoritmo "Quest?o 11"
var
   diaP, diaV: inteiro
   valorP, valorT, p: real
inicio
    EscrevaL("Informe os dados a baixo: ")
    Escreva("Dia do vencimento: ")
    Leia(diaV)
    Escreva("Dia que sendo realizado o pagamento: ")
    Leia(diaP)
    Escreva("Valor da presta??o: R$ ")
    Leia(valorP)
    Se (diaP < diaV) entao
       valorT <- valorP - (valorP*10/100)
       EscrevaL("Como voc? est? pagando em dia, ganhou 10% de desconto!")
       Escreva("Valor total ? pagar: R$ ", valorT:5:2)
    senao
       Se (diaP - diaV < 5) entao
          valorT <- valorP
          Escreva("Total ? pagar: R$ ", valorT:5:2)
       senao
          Se (diaP - diaV > 5) entao
             valorT <- valorP + (valorP*(((diaP - diaV)-5)*2)/100)
             Escreva("Valor total ? pagar: R$ ", valorT:5:2)
          fimse
       fimse
    fimse
fimalgoritmo