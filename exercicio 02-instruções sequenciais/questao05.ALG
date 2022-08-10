algoritmo "Questão 05"
var
   dia, mes, ano, diast: inteiro
inicio
    EscrevaL("Descubra quantos dias exatos você já viveu!")
    EscrevaL("Digite sua idade detalhadamente.")
    Escreva("Anos: ")
    Leia(ano)
    Escreva("Mes(es): ")
    Leia(mes)
    Escreva("Dias: ")
    Leia(dia)
    diast <- (ano * 365) + (mes * 30) + dia
    Escreva("Dias totais vividos: ", diast)
fimalgoritmo