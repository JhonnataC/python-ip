algoritmo "Quest?o 02"
var
   sexo: caractere
inicio
      Escreva("Informe o seu sexo: ")
      Leia(sexo)
      Se (sexo = "M") ou (sexo = "m") entao
         Escreva("Seu sexo ? MASCULINO. Certo?")
      senao
          Se (sexo = "F") ou (sexo = "f") entao
             Escreva("Seu sexo ? FEMININO. Certo?")
          senao
             Escreva("Informa??o inv?lida")
         fimse
      fimse
fimalgoritmo