# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímtros

med = float(input('\033[31m Coloque uma medida qualquer em metros: '))

print('\033[32m {} metros são {} centímetros.'.format(med, med*100))
print('\033[33m {} metros são {} milímetros.'.format(med, med*1000))