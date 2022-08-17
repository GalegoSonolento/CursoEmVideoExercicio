# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

maior = 0
maiorjog = 0
jogs = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
for k, v in jogs.items():
    print(f'O {k} rodou {v} no dado.')
    sleep(1)
print('-=' * 30)
apoio = jogs.copy()
print(jogs)
print(f'{"RANKING DOS JOGADORES":=^10}')
for i in range(0, len(jogs)):
    for k, v in apoio.items():
        if k == 'jogador 1':
            maior = v
            maiorjog = k
        else:
            if maior < apoio[k]:
                maior = v
                maiorjog = k
    print(f'{i+1}° lugar: {maiorjog} com {apoio[maiorjog]}')
    del apoio[maiorjog]
