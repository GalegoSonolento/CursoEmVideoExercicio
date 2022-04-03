# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27 (sdds dólares a 3 pila)

valor = float(input('\033[31m Digite seua quantia em reais: '))

dolar = valor/3.27

print('\033[32m Você pode comprar {:.2f} dólares'.format(dolar))