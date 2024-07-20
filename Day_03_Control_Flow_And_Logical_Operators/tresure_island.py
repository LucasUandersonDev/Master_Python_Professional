print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')


print("Bem vindo a ilha do tesouro")
print("Sua missão ée encontrar o tesouro")
escolha_1 = input('voce esta em uma encruzilhada, para onde você gostaria de ir? Digite "esquerda" ou "direita\n').lower()

if escolha_1 == "esquerda":
    escolha_2 = input('Você chegou a um lago. Há uma ilha no meio do lago. Digite "esperar" para esperar por um barco ou digite "nadar" para chegar a ilha nadando\n' ).lower()
    if escolha_2 == "esperar":
        escolha_3 = input('Voce chegou a ilha e encontrou tres portas a sua frente "Vermelha", "Amarela" e "Azul" escolha qual porta vai entrar\n').lower()
        if escolha_3 == "vermelho":
            print("Deu ruim")
        elif escolha_3 == "amarela":
            print("Esta rico")
        elif escolha_3 == "azul":
            print("Deu ruim")
        else:
            print("Voce foi atacado por um troll. Game over")
    else:
        print("Game Over. O jacare te pegou")
else:
    print("Game Over, caiu no buraco")


