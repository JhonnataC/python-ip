algoritmo "Questão 12"
var
    rendaA, rendaL, impo: real
    numD: inteiro
inicio
      EscrevaL("Informe os dados pedidos a baixo: ")
      Escreva("Sua renda anual: R$ ")
      Leia(rendaA)
      Escreva("Número de dependentes: ")
      Leia(numD)
      rendaL <- rendaA - ((rendaA*(numD*2))/100)
      Se (rendaL > 0) e (rendaL <= 20000) entao
         Escreva("Sem imposto aplicado")
      senao
         Se (rendaL > 20000) e (rendaL <= 50000) entao
            impo <- (rendaL*5)/100
            Escreva("Valor do imposto: R$ ", impo:8:2)
            //impo 5%
         senao
            Se (rendaL > 50000) e (rendaL <= 100000) entao
               impo <- (rendaL*10)/100
               Escreva("Valor do imposto: R$ ", impo:8:2)
               //impo 10%
            senao
               impo <- (rendaL*15)/100
               Escreva("Valor do imposto: R$ ", impo:8:2)
               //impo 15%
            fimse
         fimse
      fimse
fimalgoritmo