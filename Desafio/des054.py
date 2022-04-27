# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores (considere maioridade como 21 anos)
from datetime import date
atual = date.today().year
contMenor = 0
contMaior = 0
for i in range(1, 8):
    nasc = int(input('Digite o ano de nacimento: '))
    if (atual - nasc) >= 21:
        contMaior += 1
    else:
        contMenor += 1
print('Foram inscritos {} maiores de 21 anos'.format(contMaior), end='')
print(' e {} menores. '.format(contMenor))