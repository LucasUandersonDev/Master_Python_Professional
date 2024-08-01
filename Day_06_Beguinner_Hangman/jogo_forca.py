word_list = ["homem","casa","bicicleta","cachorro"]

import random

chosen_word = random.choice(word_list)

advinha = input("Advinha a letra: ").lower()

for letra in chosen_word:
    if letra == advinha:
        print("Certo")
    else:
        print("Wrong")