# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
# Existem bibliotecas que tem esses valores de ângulo guardados

import math
ang = float(input('\033[31m Informe o valor de um ângulo: '))
rad = math.radians(ang)
cos = math.cos(rad)
sin = math.sin(rad)
tan = math.tan(rad)
print('\033[32m O ângulo {:.3f} possui cosseno {:.3f}, seno {:.3f} e tangente {:.3f}.'.format(ang, cos, sin, tan))
