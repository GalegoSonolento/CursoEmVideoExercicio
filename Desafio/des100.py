# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    vetor = list()
    for i in range(0, 5):
        vetor.append(randint)
        print(f'{vetor[i]} ')
    print('PRONTO!')
    print()
    return vetor


def somaPar(vetor):
    print(vetor)
    # somaPares = 0
    # if type(vetor) == list:
    #     for i in range(0, len(vetor)):
    #         if vetor[i] % 2 == 0:
    #             somaPares += 1
    # print(f'Somando os valores pares de {vetor}, temos {somaPares}')


# Código principal
somaPar(sorteia())
