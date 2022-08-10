algoritmo "Questão 10"
var
  no1, no2, no3, maior, menor: caractere
  n1, n2, n3: inteiro
inicio
      Escreva("Nome: ")
      Leia(no1)
      Escreva("Idade: ")
      Leia(n1)
      Escreva("Nome: ")
      Leia(no2)
      Escreva("Idade: ")
      Leia(n2)
      Escreva("Nome: ")
      Leia(no3)
      Escreva("Idade: ")
      Leia(n3)
      Se (n1 > n2) e (n1 > n3) entao
         maior <- no1
      senao
         Se (n2 > n1) e (n2 > n3) entao
            maior <- no2
         senao
            Se (n3 > n1) e (n3 > n2) entao
              maior <- no3
            fimse
         fimse
      fimse
      Se (n1 < n2) e (n1 < n3) entao
         menor <- no1
      senao
         Se (n2 < n1) e (n2 < n3) entao
            menor <- no2
         senao
            Se (n3 < n1) e (n3 < n2) entao
              menor <- no3
            fimse
         fimse
      fimse
      EscrevaL("Quem tem maior idade? ", maior)
      EscrevaL("Quem tem menor idade? ", menor)
fimalgoritmo