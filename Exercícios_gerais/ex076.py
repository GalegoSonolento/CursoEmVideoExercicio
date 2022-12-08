# mercadinho = ("Banana Prata", 5, "Maçã Argentina", 3, "Amaciante", 10)
# for i in range(0, len(mercadinho), 2):
#     print('Produto: {: ^20} - {}'.format(mercadinho[i], mercadinho[i+1]))

listagem = ('Lápiz', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 3.20,
            'Comapsso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R$ {listagem[i]:>7.2f}')
print('-'*30)
