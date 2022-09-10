# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(ini, f, pa):
    pas = pa
    print('-='*30)
    print(f'Contagem de {ini} até {f} de {pa} em {pa}')
    if f < ini:
        f -= 2
        if pa > 0:
            pas = pa * (-1)
    for i in range(ini, f + 1, pas):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
