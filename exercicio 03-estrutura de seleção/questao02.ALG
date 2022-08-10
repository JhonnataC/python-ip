algoritmo "Questão 02"
var
   sexo: caractere
inicio
      Escreva("Informe o seu sexo: ")
      Leia(sexo)
      Se (sexo = "M") ou (sexo = "m") entao
         Escreva("Seu sexo é MASCULINO. Certo?")
      senao
          Se (sexo = "F") ou (sexo = "f") entao
             Escreva("Seu sexo é FEMININO. Certo?")
          senao
             Escreva("Informação inválida")
         fimse
      fimse
fimalgoritmo