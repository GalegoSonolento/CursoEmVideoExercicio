# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa

import math
catop = float(input('Informe o cateto oposto: '))
catad = float(input('Informe o cateto adjacente: '))

hip = math.sqrt(math.pow(catop, 2)+math.pow(catad, 2))
print('Sua hipotenusa é: {}'.format(hip))
