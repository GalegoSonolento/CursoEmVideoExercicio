# Crie um programa que leia um número real pelo teclado e mostre na tela sua porção inteira
# Ex.: Digite um número: 6.127
# o número tal tem parte inteira 6
# Dá pra usar math

import math
num = float(input('Digite um número: '))
ptReal = math.trunc(num)
print(ptReal)
