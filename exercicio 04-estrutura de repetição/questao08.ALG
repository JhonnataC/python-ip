algoritmo "Questão 08"
var
   qkwh, val: real
   cod: inteiro
inicio
      cod <- 1
      Enquanto (cod <> 0) faca
              EscrevaL("[1] residencial")
              EscrevaL("[2] comercial")
              EscrevaL("[3] industrial")
              EscrevaL("[0] sair do programa")
              EscrevaL("====================")
              Escreva("Informe o seu código de consumo: ")
              Leia(cod)
              Se (cod = 1) ou (cod = 2) ou (cod = 3) entao
              EscrevaL("Quantide de kWh gastos no mês: ")
              Leia(qkwh)
              Se (cod = 1) entao
                 EscrevaL("Residencial")
                 val <- qkwh * 0.85
                 Se (qkwh <= 30) entao
                    val <- val - (val*20/100)
                 fimse
                 EscrevaL("Total à pagar: R$ ", val)
                 limpatela
              senao
                 Se (cod = 2) entao
                    EscrevaL("Comercial")
                    val <- qkwh * 0.35
                    Se (qkwh > 30) e (qkwh <= 100) entao
                       val <- val - (val*20/100)
                    fimse
                    EscrevaL("Total à pagar: R$ ", val)
                    limpatela
                    senao
                       Se (cod = 3) entao
                          EscrevaL("Industrial")
                          val <- qkwh * 0.10
                          Se (qkwh > 100) e (qkwh <= 200) entao
                             val <- val - (val*20/100)
                          fimse
                          EscrevaL("Total à pagar: R$ ", val)
                          limpatela
                       fimse
                 fimse
              fimse
              fimse
      fimenquanto

fimalgoritmo