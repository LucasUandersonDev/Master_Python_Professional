import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Qual é sua escolha? Digite 0 para pedra, 1 para papel e 2 para tesoura.\n"))
#print(game_images[user_choice])

#correção do bug
if user_choice >= 3 or user_choice < 0:
    print("Deu mole numero fora, voce perdeu.")
else:
    print(game_images[user_choice])


computer_choice = random.randint(0, 2)
print("computer chose:")
print(game_images[computer_choice])



if user_choice >= 3 or user_choice < 0:
    print("Você digitou um numero invalido, você perdeu!")
elif user_choice == 0 and computer_choice == 2:
    print("Você venceu")
elif computer_choice == 0 and user_choice == 2:
    print("Voce perdeu")
elif computer_choice > user_choice:
    print("Você perdeu")
elif user_choice > computer_choice:
    print("voce venceu")
elif computer_choice == user_choice:
    print("Deu empate")
    




