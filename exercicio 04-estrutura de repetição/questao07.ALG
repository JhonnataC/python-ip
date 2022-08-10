algoritmo "Questão 07"
var
   a, b, c, d, n, br, tot, vot: inteiro
   pa, pb, pc, pd, pn, pbr: real
inicio
      vot <- 1
      Enquanto (vot <> 0) faca
               limpatela
               EscrevaL("Digite o número do seu candidato: ")
               Leia(vot)
               Se (vot = 1) entao
                  EscrevaL("Voto no candidato 1")
                  a <- a + 1
                  tot <- tot + 1
               senao
                  Se (vot = 2) entao
                     EscrevaL("Voto no candidato 2")
                     b <- b + 1
                     tot <- tot + 1
                  senao
                     Se (vot = 3) entao
                        EscrevaL("Voto no candidato 3")
                        c <- c + 1
                        tot <- tot + 1
                     senao
                        Se (vot = 4) entao
                        EscrevaL("Voto no candidato 4")
                           d <- d + 1
                           tot <- tot + 1
                        senao
                           Se (vot = 5) entao
                           EscrevaL("Voto nulo")
                              n <- n + 1
                              tot <- tot + 1
                           senao
                              Se (vot = 6) entao
                                 EscrevaL("Voto em branco")
                                 br <- br + 1
                                 tot <- tot + 1
                              fimse
                           fimse
                        fimse
                     fimse
                  fimse
               fimse
      fimenquanto
      pa <- a*100/tot
      pb <- b*100/tot
      pc <- c*100/tot
      pd <- d*100/tot
      pn <- n*100/tot
      pbr <- br*100/tot
      EscrevaL("Sessão encerrada")
      EscrevaL("================")
      EscrevaL("Votos do canditado 1: ", a, ". Porcentagem: ", pa:4:2,"%")
      EscrevaL("Votos do canditado 2: ", b, ". Porcentagem: ", pb:4:2,"%")
      EscrevaL("Votos do canditado 3: ", c, ". Porcentagem: ", pc:4:2,"%")
      EscrevaL("Votos do canditado 4: ", d, ". Porcentagem: ", pd:4:2,"%")
      EscrevaL("Votos nulos: ", n, ". Porcentagem: ", pn:4:2,"%")
      EscrevaL("Votos brancos: ", br, ". Porcentagem: ", br:4:2,"%")
fimalgoritmo