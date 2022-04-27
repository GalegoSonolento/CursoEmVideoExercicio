# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso de uma pessoa em quilogramas: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi {} e o menor foi {}'.format(maior, menor))
