# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

mercadinho = ("Banana Prata", 5, "Maçã Argentina", 3, "Amaciante", 10)
for i in range(0, len(mercadinho), 2):
    print('Produto: {: ^20} - {}'.format(mercadinho[i], mercadinho[i+1]))
