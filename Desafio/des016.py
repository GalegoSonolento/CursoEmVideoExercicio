# Crie um programa que leia um número real pelo teclado e mostre na tela sua porção inteira
# Ex.: Digite um número: 6.127
# o número tal tem parte inteira 6
# Dá pra usar math

import math
num = float(input('\033[1;30;46m Digite um número: \033[m'))
ptReal = math.trunc(num)
print(ptReal)
