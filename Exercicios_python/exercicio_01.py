'''
Desafio 1: Números Primos
Objetivo: Escrever uma função que verifique se um número é primo.

Instruções:
Crie uma função chamada eh_primo que receba um número inteiro como argumento.
A função deve retornar True se o número for primo e False caso contrário.
Dicas:
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
Você pode usar a função range() para gerar uma sequência de números para verificar divisibilidade.

Exemplo:

print(eh_primo(7))  # Deve retornar True
print(eh_primo(10)) # Deve retornar False

Quando terminar, envie sua solução ou me avise se precisar de ajuda!

'''

def eh_primo(numero):
    if numero <= 1:
        return False
    
    for num in range(2, int(numero ** 0.5) + 1):
        if numero % num == 0:
            return False
    return True


print(eh_primo(2))
print(eh_primo(10))