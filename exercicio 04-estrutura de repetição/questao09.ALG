algoritmo "Questão 09"
var
   ham, che, bat, ref, cont: real
   cod: inteiro
inicio
    cod <- 1
    Enquanto (cod <> 5) faca
            EscrevaL("=================")
            EscrevaL("[1] Hamburguer")
            EscrevaL("[2] Cheeseburguer")
            EscrevaL("[3] Batata frita")
            EscrevaL("[4] Refrigerante")
            EscrevaL("[5] Para fechar a conta")
            EscrevaL("=================")
            Leia(cod)
            Se (cod <> 5) entao
               Se (cod = 1) entao
                  ham <- ham + 1
                  EscrevaL("Hamburguer adicionado à conta!")
                  limpatela
               senao
                  Se (cod = 2) entao
                     che <- che + 1
                     EscrevaL("Cheeseburguer adicionado à conta!")
                     limpatela
                  senao
                     Se (cod = 3) entao
                        bat <- bat + 1
                        EscrevaL("Batata frita adicionado à conta!")
                        limpatela
                     senao
                        Se (cod = 4) entao
                           ref <- ref + 1
                           EscrevaL("Refrigerante adicionado à conta!")
                           limpatela
                        fimse
                     fimse
                  fimse
               fimse
            fimse
    fimenquanto
    cont <- (ham * 2.50) + (che * 3.30) + (bat * 1.50) + (ref * 0.60)
    EscrevaL("Conta: R$ ", cont:5:2)
fimalgoritmo