# Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
maior = menor = 0
multiplicador = 100
teste = [int(random.random() * multiplicador), int(random.random() * multiplicador), int(random.random() * multiplicador), int(random.random() * multiplicador), int(random.random() * multiplicador)]
for i in range(len(teste)):
    print(f'- {teste[i]}', end=' ')
    print(' ')
    if i == 0:
        maior = menor = teste[i]
    else:
        if maior < teste[i]:
            maior = teste[i]
        if menor > teste[i]:
            menor = teste[i]
print(f'O menor valor é {menor} e o maior é {maior}')