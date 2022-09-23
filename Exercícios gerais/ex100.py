# # Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
# # sorteia() e somaPar().
# # A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# # e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
#
# from random import randint
#
#
# def sorteia():
#     print('Sorteando 5 valores da lista: ', end='')
#     vetor = []
#     for i in range(0, 5):
#         vetor.append(randint(1, 10))
#         print(f'{vetor[i]} ', end='')
#     print('PRONTO!')
#     return vetor
#
#
# def somaPar(vetor):
#     somaPares = 0
#     if type(vetor) == list:
#         for i in range(0, len(vetor)):
#             if vetor[i] % 2 == 0:
#                 somaPares += vetor[i]
#     print(f'Somando os valores pares de {vetor}, temos {somaPares}')
#
#
# # Código principal
# somaPar(sorteia())
#
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        lista.append(randint(1, 10))  # Sempre lembrar de colocar o range do randint
        print(f'{lista[cont]}', end=' ')  # Esse método de amostragem por indexação é muito utilizado
        sleep(0.3)
    print('PRONTO')


def somaPar(lista):  # Diferente de mim, ele trocou todos os pontos de memória do vetor
    soma = 0
    for valor in lista: # Iteração simples
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteia(num)
somaPar(num)
