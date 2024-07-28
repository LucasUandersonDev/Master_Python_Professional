'''
Exercício 2: FizzBuzz
Descrição:
Crie uma função chamada fizz_buzz que recebe um número inteiro como entrada. A função deve retornar:

"Fizz" se o número for divisível por 3,
"Buzz" se o número for divisível por 5,
"FizzBuzz" se o número for divisível por 3 e 5,
O próprio número se ele não for divisível nem por 3 nem por 5.
Requisitos:

Use a operação de módulo (%) para verificar a divisibilidade.
Certifique-se de que a função retorne corretamente para todos os casos mencionados.
Dicas:

Você pode usar a função print para exibir os resultados enquanto testa a função.
Teste sua função com vários números diferentes para garantir que todos os casos estão cobertos.
Exemplo de Saída Esperada:
python
Copiar código
print(fizz_buzz(3))    # Deve retornar "Fizz"
print(fizz_buzz(5))    # Deve retornar "Buzz"
print(fizz_buzz(15))   # Deve retornar "FizzBuzz"
print(fizz_buzz(7))    # Deve retornar 7
'''

def fizz_buzz (numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero



num1 = 20


for num in range(1, num1 + 1):
    print(fizz_buzz(num))




print(fizz_buzz(3))    # Deve retornar "Fizz"
print(fizz_buzz(5))    # Deve retornar "Buzz"
print(fizz_buzz(15))   # Deve retornar "FizzBuzz"
print(fizz_buzz(7))    # Deve retornar 7



