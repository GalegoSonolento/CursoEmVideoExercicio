# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.

dias = int(input('Por quantos dias você alugaou o carro? R$'))
km = float(input('Quantos quilômetros foram rodados? R$'))

valor = (dias * 60) + (km * 0.15)

print('Você pagará {} reais pelo aluguel do carro'.format(valor))