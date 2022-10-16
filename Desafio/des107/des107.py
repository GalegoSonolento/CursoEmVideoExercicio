import moeda

num = float(input('Digite o preço: '))
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num)}')
print(f'Diminuindo 10%, temos {moeda.diminuir(num)}')
