# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    totGols = 0
    for i in range(0, quant):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
        totGols += gols[i]
    jogador['gols'] = gols[:]
    jogador['total'] = totGols
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda com S ou N.')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"cod nome":<17}{"gols"}{"total":>15}')
print('-'*50)
for i in range(0, len(time)):
    # print(f'{time[i]["gols"]}')
    print(f'  {i} {time[i]["nome"]:<13}{time[i]["gols"]}{time[i]["total"]:^11}')
print('-'*50)
while True:
    jog = int(input('Mostrar levantamento de qual jogador? (999 para parar) '))
    if jog == 999:
        break
    elif jog > len(time):
        print(f'ERRO! Não existe jogador com o código {jog}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[jog]["nome"]}: ')
        for i in range(0, len(time[jog]["gols"])):
            print(f'    Na partida {i + 1} fez {jogador["gols"][i]} gols')
print('<<< VOLTE SEMPRE >>>')

