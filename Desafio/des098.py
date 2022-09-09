# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    pas = passo
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim < inicio:
        pas = passo*(-1)
    for i in range(inicio, fim+1, pas):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!')
    print()

def umem1():
    print('-='*30)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
