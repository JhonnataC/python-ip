algoritmo "Quest?o 08"
var
   v1, v2, area: real
inicio
      EscrevaL("Calculador de ?rea de terrenos")
      Escreva("1? medida: ")
      Leia(v1)
      Escreva("2? medida: ")
      Leia(v2)
      Se (v1 = v2) entao
         EscrevaL("Terreno quadrado")
         area <- v1*v2
         Escreva("Tamanho: ", area)
      senao
         EscrevaL("Terreno ret?ngular")
         area <- v1*v2
         Escreva("Tamanho: ", area)
      fimse
fimalgoritmo