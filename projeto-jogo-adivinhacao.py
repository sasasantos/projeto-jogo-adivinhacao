import random
import os

# limpando tela
os.system("cls")

# entrada de dados

print("====================== JOGO DE ADIVINHAÇÃO ======================")
print(" O sistema escolhera um número de 0 a 100. Tente adivinhar qual será! \n")

palpite = int(input("Insira seu número: "))

#processamento de dados

NumeroSistema = random.randint(0, 101)

tentativas = 0

while(tentativas <= 3):
      if(palpite < NumeroSistema):
        print("O número que você digitou é menor que o NÚMERO SECRETO. Pressione <Enter> para tentar novamente. \n")
        palpite = int(input("Nova tentativa: "))
        tentativas +=1

      elif(palpite > 100):
          print("O valor que você digitou está acima do aceitavel (número maximo 100). \n")
          palpite = int(input("Nova tentativa: "))
          tentativas +=1
         
      elif(palpite > NumeroSistema):   
          print("O numero que voce digitou é maior que o NÚMERO SECRETO. Pressione <Enter> para tentar novamente. \n")
          palpite = int(input("Nova tentativa: "))
          tentativas +=1
      
      elif(palpite == NumeroSistema):
        input("VOCÊ ACERTOU! Meus parabens. \n") 
        tentativas +=1
        break

print(f"Fim de jogo, você utilizou o total de {tentativas} tentativas!")