algoritmo "Quest?o 06"
var
   nome: caractere
   sal, nsal, porc: real
inicio
    Escreva("Nome do funcion?rio: ")
    Leia(nome)
    Escreva("Informe o seu sal?rio atual: R$ ")
    Leia(sal)
    Se (sal > 0) e (sal <= 400) entao
       nsal <- sal + sal*15/100
       porc <- 15
    senao
       Se (sal > 400) e (sal <= 700) entao
          nsal <- sal + sal*12/100
          porc <- 12
       senao
          Se (sal > 700) e (sal <= 1000) entao
             nsal <- sal + sal*10/100
             porc <- 10
          senao
             Se (sal > 1000) e (sal <= 1800) entao
                nsal <- sal + sal*7/100
                porc <- 7
             senao
                Se (sal > 1800) e (sal <= 2500) entao
                   nsal <- sal + sal*4/100
                   porc <- 4
                senao
                   nsal <- sal
                   porc <- 0
                fimse
             fimse
          fimse
       fimse
    fimse
    EscrevaL("Funcion?rio: ", nome)
    EscrevaL("Porcentagem de aumento: ", porc,"%")
    EscrevaL("Sal?rio atual: R$ ", sal)
    Escreva("Sal?rio novo: R$ ", nsal)
fimalgoritmo