#Jogo Pedra, Papel e Tesoura
# GITHUB

from random import randint
from time import sleep 


for i in range(3):
    possibilidades=("Pedra","Papel","Tesoura")
    maquina = randint(0,2)

    print("<>"*15)
    print("0 - Pedra \n "+"1 - Papel \n " + "2 - Tesoura ")
    Jogador=int(input("Qual voce deseja?"))
    print("<>"*15)
    print("JO")
    sleep(3)
    print("KEN")
    sleep(3)
    print("PO")
    sleep(3)
    print("Computador Jogou {}".format(possibilidades[maquina]))
    print(" Voce      Jogou {}".format(possibilidades[Jogador]))

    if maquina==0:
    #pedra
        if Jogador ==0:
          print ("Empate")

        elif Jogador==1:
          print ("Jogador Venceu") 

        elif Jogador==2:
          print("Computador Venceu")


    elif maquina==1:
      #Papel
          if Jogador==0:
            print("Computador Venceu") 
          elif Jogador==1:
            print("Empate")
          elif Jogador==2:
            print("Jogador Venceu")

    elif maquina==2:
      #Tesoura
          if Jogador==0:
            print("Jogador Venceu")
          elif Jogador==1:
            print("Computador Venceu")
          elif Jogador==2:
            print("Empate")

    else:
       print("Movimento Inválido") 


print("\n")
print("\n")
print("\n")

