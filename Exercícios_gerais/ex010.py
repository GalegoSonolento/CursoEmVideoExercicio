real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 5.08
euro = real / 5.54
print('Com {:.2f} você pode comprar {:.2f} dólares no dia 12/03/2022'.format(real, dolar))
print('Mas com {:.2f} você pode comprar {:.2f} euros no dia 12/03/2022'.format(real, euro))