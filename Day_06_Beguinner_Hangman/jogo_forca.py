import random
from hangman_words import word_list
from hangman_art import logo,stages


end_of_game = False 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(logo)
print(f"Pssst, a solução é {chosen_word}")

display = []
for _ in range(word_length):
    display +="_"

while not end_of_game:
    guess = input("Advinhe a letra").lower()

    if guess in display:
        print(f"Você já adivinhou {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Você adivinhou {guess}, isso não está na palavra. Você perde uma vida. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Você perdeu")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("Você venceu")
    
    print(stages[lives])



