# # Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# # Guarde esses resultados em um dicionário em Python.
# # No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
#
# from random import randint
# from time import sleep
#
# jogs = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6),
#         'jogador 4': randint(1, 6)}
# for k, v in jogs.items():
#     print(f'O {k} rodou {v} no dado.')
#     sleep(1)
# print('-=' * 30)
# apoio = jogs.copy()
# print(f'{"RANKING DOS JOGADORES":=^10}')
# for i in range(0, len(jogs)):
#     maior = 0
#     maiorjog = 0
#     for k, v in apoio.items():
#         if k == 'jogador1':
#             maior = v
#             maiorjog = k
#         else:
#             if maior < apoio[k]:
#                 maior = v
#                 maiorjog = k
#     print(f'{i+1}° lugar: {maiorjog} com {apoio[maiorjog]}')
#     del apoio[maiorjog]

from random import randint
from time import sleep
from operator import itemgetter     # Esses operadores são API's do python
jogo = { 'jogador1': randint(1, 6),     # Realiza todo o sorteio dos jogadores
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = dict()    # Dicionário vazio pra apoio
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')    # Mostra os resultados do sorteio
    sleep(1)    # Tempo de espera pra leitura
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)   # Essa é uma forma de sorteio que escolhe qual ítem
# ordenar (key ou value)
# print(ranking)  # Esse resultado é printado em forma de lista, não de dicionário (ele tem várias tuplas)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar {v[0]} com {v[1]}.')   # Por se transformar em lista, ranking deve ser tratado como uma
    sleep(1)


































