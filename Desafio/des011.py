# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabenedo que cada litro de tinta pinta uma área de 2m²

alt = float(input('\033[31m Dê a altura da sua parede: '))
larg = float(input('\033[32m Dê a largura da sua parede: '))

apar = alt*larg
litros = apar/2

print('\033[33m Você precisa de {} litros de tinta.'.format(litros))