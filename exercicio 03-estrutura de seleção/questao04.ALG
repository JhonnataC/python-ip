algoritmo "Questão 04"
var
   n1, n2, media: real
inicio
    Escreva("Digite a 1° nota: ")
    leia(n1)
    Escreva("Digite a 2° nota: ")
    leia(n2)
    media <- (n1 + n2) / 2
    Se (media = 10) entao
       Escreva("Aluno aprovado com distinção!")
    senao
       Se (media >= 7) e (media < 10) entao
          Escreva("Aluno aprovado!")
       senao
          Escreva("Aluno reprovado!")
       fimse
    fimse
fimalgoritmo