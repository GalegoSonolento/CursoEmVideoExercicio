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

from time import sleep


def maior(* num):   # A expressão em parênteses cria tuplas dentro da def (empacota os dados recebidos no chamamento do
    # método)
    cont = maior = 0    # Variáveis de apoio
    print('-='*30)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(1, 2)
maior(6)
maior()
