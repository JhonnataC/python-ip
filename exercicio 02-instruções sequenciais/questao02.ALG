algoritmo "Quest?o 02"
var
   pares, sap, temp: inteiro
   din: real
inicio
    Escreva("Quantidade de pares que deseja engraxar: ")
    Leia(pares)
    sap <- pares*2
    temp <- sap*sap
    din <- pares*25
    EscrevaL("===================================")
    EscrevaL("N?mero de sapatos para engraxar: ", sap,".")
    EscrevaL("Tempo necess?rio para engraxar: ", temp, " minutos.")
    EscrevaL("Custo total: R$ ", din:4:2, ".")
fimalgoritmo