algoritmo "Questão 07"
var
   nome: caractere
   idade, valor, val: inteiro
inicio
      EscrevaL("Descubra o valor do seu plano de saúde.")
      Escreva("Nome: ")
      Leia(nome)
      Escreva("Idade: ")
      Leia(idade)
      Se (idade < 10) entao
         val <- 30
      senao
         Se (idade > 10) e (idade <= 29) entao
            val <- 60
         senao
            Se (idade > 29) e (idade <= 45) entao
               val <- 120
            senao
               Se (idade > 45) e (idade <= 59) entao
                  val <- 150
               senao
                  Se (idade > 59) e (idade <= 65) entao
                     val <- 250
                  senao
                     val <- 400
                  fimse
               fimse
            fimse
         fimse
      fimse
      EscrevaL("Cliente: ", nome)
      Escreva("Valor mensal do plano: R$ ", val)
fimalgoritmo