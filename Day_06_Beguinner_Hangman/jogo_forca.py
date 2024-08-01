import random
word_list = ["homem","casa","bicicleta","cachorro"]
chosen_word = random.choice(word_list)

print(f"Pssst, a solução é {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
    

guess = input("Advinha a letra: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
        
print(display)
    