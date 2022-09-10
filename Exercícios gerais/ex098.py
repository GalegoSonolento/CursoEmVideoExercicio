# # Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# # fim e passo.
# # Seu programa tem que realizar três contagens através da função criada:
# # a) de 1 até 10, de 1 em 1
# # b) de 10 até 0, de 2 em 2
# # c) uma contagem personalizada
#
# from time import sleep
#
#
# def contador(ini, f, pa):
#     pas = pa
#     print('-='*30)
#     print(f'Contagem de {ini} até {f} de {pa} em {pa}')
#     if f < ini:
#         f -= 2
#         if pa > 0:
#             pas = pa * (-1)
#     for i in range(ini, f + 1, pas):
#         print(f'{i}', end=' ')
#         sleep(0.5)
#     print('FIM!')
#
#
# contador(1, 10, 1)
# contador(10, 0, 2)
# print('-='*30)
# print('Agora é sua vez de personalizar a contagem!')
# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))
# contador(inicio, fim, passo)
from time import sleep
# Um atalho legal para as dicas da IDE é o Alt+Enter e o Ctrl+Alt+Shift+T -> ele dá algumas opções de refatoração
# Dá pra puxar as bibliotecas automaticamente tbm


def contador(ini, fim, pas):
    print('-='*20)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    sleep(2.5)
    if pas < 0:     # Esses dois if impedem o loop eterno do programa
        pas *= -1
    if pas == 0:
        pas = 1
    if ini < fim:
        cont = ini
        while cont <= fim:  # Um tipo de solução comum mas pouco aplicável à maioria dos casos de código
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += pas
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= pas
    print('Fim!')
    print('-='*20)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fin = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fin, passo)    # Um passo negativo quebra um programa sem a refatoração necessária
