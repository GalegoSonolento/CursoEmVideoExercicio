# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonate Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: a) Apenas os 5 primeiros colocados.
# b) os 4 últimos colocados.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.

brasileirao = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Santos', 'Fluminense',
               'Coritiba', 'América Mineiro', 'Avaí', 'Internacional', 'Athletico-PR', 'Bragantino',
               'Flamengo', 'Goiás', 'Cuiabá', 'Atlético Goianiense', 'Juventude', 'Ceará', 'Fortaleza')
print('Cinco primeiros colocados: ')
for i in range(len(brasileirao)):
    if i < 5:
        print(brasileirao[i])
print(' ')
print('Quatro últimos colocados:')
for i in range(len(brasileirao)):
    if i > 15:
        print(brasileirao[i])
print(' ')
print('Tabela em ordem alfabética')
tabelado = sorted(brasileirao)
for i in range(len(tabelado)):
    print(f'- {tabelado[i]}')
print(' ')
print('Posição da Chapecoense')
temChape = False
for i in range(len(brasileirao)):
    if brasileirao == 'Chapecoense':
        print(f'A Chapecoense está na {i+1}° posição')
        temChape = True
        break
if not temChape:
    print('A Chapecoense não está na série A')
