# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto

preco = float(input('Dê o preço do produto: '))
desconto = preco*0.05

print('Com  desconto o produto fica: {}'.format(preco-desconto))