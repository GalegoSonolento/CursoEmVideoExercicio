# # Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# # que receba vários parâmetros com valores inteiros.
# # Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# from time import sleep
#
#
# def maior(* num):
#     print('-='*30)
#     high = 0
#     for i, j in enumerate(num):
#         if i == 0:
#             high = j
#         if j > high:
#             high = j
#     print('Analisando os valores passados...')
#     sleep(1)
#     for i in range(0, len(num)):
#         print(i, end=' ')
#     print()
#     print(f'Foram informados {len(num)} valores ao todo. \n'
#           f'O maior valor informado foi {high}')
#
#
# # Corpo principal
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()


def maior(* num):
    cont = maior = 0
    print('\n Analisando os valores passados...')
    for v in num:
        print(f'{v}', end=' ')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(1, 2)
maior()
maior(6)




































