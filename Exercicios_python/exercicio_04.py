'''
Objetivo:
Escreva um programa em Python que calcule a soma dos números de 1 até um número N fornecido pelo usuário.

Instruções:

Solicite ao usuário que insira um número inteiro positivo N.
Use um loop para somar todos os números de 1 até N.
Exiba o resultado da soma.
Dica:
Você pode usar a função input() para obter a entrada do usuário e converter a entrada para um número inteiro com int(). Use um loop for ou while para realizar a soma.
'''


user = int(input("Digite um numero"))

soma = 0 

for number in range (1, user +1):  
    soma += number



print(f"A soma dos números de 1 até {user} é: {soma}")


