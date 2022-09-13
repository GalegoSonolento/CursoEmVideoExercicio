# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* num):
    print('-='*30)
    high = 0
    for i, j in enumerate(num):
        if i == 0:
            high = j
        if j > high:
            high = j
    print('Analisando os valores passados...')
    sleep(1)
    print(f'Foram informados {len(num)} valores ao todo. \n' 
          f'O maior valor informado foi {high}')


# Corpo principal