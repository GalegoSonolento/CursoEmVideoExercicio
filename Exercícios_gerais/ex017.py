# co = float(input('Comprimento cateto oposto: '))
# ca = float(input('Comprimento cateto adjacente: '))
# hp = (co**2 + ca ** 2) ** (1/2)
# print('Hipotenusa vale {:.2f}'.format(hp))
from math import hypot
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
hp = hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hp))
