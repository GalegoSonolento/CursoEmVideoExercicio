# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa

import math
catop = float(input('\033[30m Informe o cateto oposto: '))
catad = float(input('\033[31m Informe o cateto adjacente: '))

hip = math.sqrt(math.pow(catop, 2)+math.pow(catad, 2))
print('\033[32m Sua hipotenusa é: {}'.format(hip))
