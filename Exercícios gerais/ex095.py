# # Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# # incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
#
# time = list()
# jogador = dict()
# gols = list()
# while True:
#     jogador.clear()
#     gols.clear()
#     jogador['nome'] = str(input('Nome do jogador: '))
#     quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     totGols = 0
#     for i in range(0, quant):
#         gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
#         totGols += gols[i]
#     jogador['gols'] = gols[:]
#     jogador['total'] = totGols
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('Quer continuar? [S/N] ')).upper()[0]
#         if resp in 'SN':
#             break
#         print('ERRO! Responda com S ou N.')
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'{"cod nome":<17}{"gols"}{"total":>15}')
# print('-'*50)
# for i in range(0, len(time)):
#     # print(f'{time[i]["gols"]}')
#     print(f'  {i} {time[i]["nome"]:<13}{time[i]["gols"]}{time[i]["total"]:^11}')
# print('-'*50)
# while True:
#     jog = int(input('Mostrar levantamento de qual jogador? (999 para parar) '))
#     if jog == 999:
#         break
#     elif jog > len(time):
#         print(f'ERRO! Não existe jogador com o código {jog}!')
#     else:
#         print(f' -- LEVANTAMENTO DO JOGADOR {time[jog]["nome"]}: ')
#         for i in range(0, len(time[jog]["gols"])):
#             print(f'    Na partida {i + 1} fez {jogador["gols"][i]} gols')
# print('<<< VOLTE SEMPRE >>>')
#

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {i+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0] # Esse método das lista do python (sum) salva uma iteração de cálculo q seria
        if resp in 'SsNn': # colocada junto do preenchimento da lista das partidas (num programa grande ela salva espaços de memória)
            break
        print('ERRO! Responda com S ou N.')
    if resp == 'N':
        break
print('-='*30)  # Até aqui é só a leitura de dados, depois dessa linha, surge a análise de dados
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end=' ')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, v in enumerate(jogador["gols"]):
            print(f'    Na partida {i+1} fez {jogador["gols"][i]} gols')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')
