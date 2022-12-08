# brasileirao = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Santos', 'Fluminense',
#                'Coritiba', 'América Mineiro', 'Avaí', 'Internacional', 'Athletico-PR', 'Bragantino',
#                'Flamengo', 'Goiás', 'Cuiabá', 'Atlético Goianiense', 'Juventude', 'Ceará', 'Fortaleza')
# print('Cinco primeiros colocados: ')
# for i in range(len(brasileirao)):
#     if i < 5:
#         print(brasileirao[i])
# print(' ')
# print('Quatro últimos colocados:')
# for i in range(len(brasileirao)):
#     if i > 15:
#         print(brasileirao[i])
# print(' ')
# print('Tabela em ordem alfabética')
# tabelado = sorted(brasileirao)
# for i in range(len(tabelado)):
#     print(f'- {tabelado[i]}')
# print(' ')
# print('Posição da Chapecoense')
# temChape = False
# for i in range(len(brasileirao)):
#     if brasileirao == 'Chapecoense':
#         print(f'A Chapecoense está na {i+1}° posição')
#         temChape = True
#         break
# if not temChape:
#     print('A Chapecoense não está na série A')

brasileirao = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Santos', 'Fluminense',
                'Coritiba', 'América Mineiro', 'Avaí', 'Internacional', 'Athletico-PR', 'Bragantino',
                'Flamengo', 'Goiás', 'Cuiabá', 'Atlético Goianiense', 'Juventude', 'Ceará', 'Fortaleza')
print(f'Lista de times: {brasileirao}')
# for i in brasileirao:
#     print(i)
print('='*15)
print(f'Os cinco primeiros são {brasileirao[0:5]}')
print('='*15)
print(f'Os quatro últimos são: {brasileirao[-4:]}')
print('='*15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('='*15)
# print(f'O chapecoense está na {print(brasileirao.index("Chapecoense")) if brasileirao.index("Chapecoense") < 0 else print(-1)} posição')
# A chapecoense não está no campeonato esse ano (2022), então eu preciso usar o método do exercício.
temChape = False
for i in range(len(brasileirao)):
    if brasileirao == 'Chapecoense':
        print(f'A Chapecoense está na {i+1}° posição')
        temChape = True
        break
if not temChape:
    print('A Chapecoense não está na série A')
