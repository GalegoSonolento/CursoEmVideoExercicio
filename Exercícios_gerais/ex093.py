# # Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# # O programa vai ler o nome do jogador e quantas partidas ele jogou.
# # Depois vai ler a quantidade de gols feitos em cada partida.
# # No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
#
# jogador = dict()
# gols = list()
# jogador['nome'] = str(input('Nome do jogador: '))
# quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# totGols = 0
# for i in range(0, quant):
#     gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
#     totGols += gols[i]
# jogador['gols'] = gols[:]
# jogador['total'] = totGols
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem valor {v}')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {quant} partidas: ')
# for i in range(0, quant):
#     print(f'    => Na partida {i+1} fez {jogador["gols"][i]} gols')
# print(f'Foi um total de {totGols} gols')

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {i+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)    # Esse método das lista do python (sum) salva uma iteração de cálculo q seria
# colocada junto do preenchimento da lista das partidas (num programa grande ela salva espaços de memória)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')     # Aqui ele começa a abrir mão de
# variáveis auxiliares. O truque de usar len para ler o tamanho da lista e, assim, saber quantos jogos eram, foi algo
# que não pensei
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1} fez {jogador["gols"][i]} gols')
print(f'Foi um total de {jogador["total"]} gols')


































