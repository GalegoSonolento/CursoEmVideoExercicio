from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
radians(angulo)
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {} tem seno {:.3f}, cosseno {:.3f} e tangente {:.1f}'.format(angulo, seno, cosseno, tangente))
