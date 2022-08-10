algoritmo "Questão 01"
var
   alt, larg, comp, vol: real
inicio
    EscrevaL("Informe as medidas pedidas a baixo para saber o volume.")
    Escreva("Altura(m): ")
    Leia(alt)
    Escreva("Largura(m): ")
    Leia(larg)
    Escreva("Comprimento(m): ")
    Leia(comp)
    vol <- alt*larg*comp
    Escreva("Volume: ", vol," m3")
fimalgoritmo