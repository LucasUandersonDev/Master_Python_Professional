import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao PyPassword Generator")

nr_letters = int(input("Quantas letras gostaria em sua senha?\n"))
nr_symbols = int(input("Quantos simbolos gostaria em sua senha?\n"))
nr_numbers = int(input("Quantos numeros gostaria em sua senha?\n"))

#password = ""

#for char in range(1, nr_letters + 1):
    #password += random.choice(letters)

#for char in range(1, nr_symbols + 1):
    #password += random.choice(symbols)

#for char in range(1, nr_numbers + 1):
    #password += random.choice(numbers)


#print(password)

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
# Lembrando que tanto append ou += adicionam itens a lista
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list: 
    password += char

print(f"Sua senha é: {password}")