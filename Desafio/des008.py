# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímtros

med = float(input('Coloque uma medida qualquer em metros: '))

print('{} metros são {} centímetros.'.format(med, med*100))
print('{} metros são {} milímetros.'.format(med, med*1000))