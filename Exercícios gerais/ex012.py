preco = float(input('Qual o preço do produto? $'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f} fica R${:.2f} com a promoção'.format(preco, novo))
