algoritmo "Quest?o 09"
var
   cargo: caractere
   sal, nsal, porc: real
inicio
    Escreva("Cargo: ")
    Leia(cargo)
    Escreva("Informe o seu sal?rio atual: R$ ")
    Leia(sal)
    Se (cargo = "escritur?rio") entao
       nsal <- sal + sal*50/100
       porc <- 50
    senao
       Se (cargo = "secret?rio") entao
          nsal <- sal + sal*35/100
          porc <- 35
       senao
          Se (cargo = "caixa") entao
             nsal <- sal + sal*20/100
             porc <- 20
          senao
             Se (cargo = "gerente") entao
                nsal <- sal + sal*10/100
                porc <- 10
             senao
                Se (cargo = "diretor") entao
                   nsal <- sal
                   porc <- 0
                fimse
             fimse
          fimse
       fimse
    fimse
    EscrevaL("============================")
    EscrevaL("Cargo: ", cargo)
    EscrevaL("Porcentagem de aumento: ", porc,"%")
    EscrevaL("Sal?rio atual: R$ ", sal)
    Escreva("Sal?rio novo: R$ ", nsal)
fimalgoritmo