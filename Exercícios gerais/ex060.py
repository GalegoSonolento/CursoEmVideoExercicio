# #Faça um program que leia um número qualquer e mostre seu fatorial
# # 5! = 5.4.3.2.1 = 120
# # Fazer com while e outro com for
#
# # fator = int(input('Digite um número para realizar o fatorial: '))
# # cont = fator - 1
# # fatorial = fator
# # while cont != 1:
# #     if cont == fator - 1:
# #         fatorial = fator * cont
# #         cont -= 1
# #     else:
# #         fatorial = fatorial * cont
# #         cont -= 1
# # print('O fatorial de {} é {}'.format(fator, fatorial))
#
# fator = int(input('Digite um número para realizar o fatorial: '))
# fatorial = fator
# for i in range(1, fator):
#     fatorial = fatorial * i
# print('Fatorial de {} é {}'.format(fator, fatorial))

# ==-=-=-==-==-==-==-=-==-==-=-==-==-==-==-==-==-==-==

# from math import factorial
# n = int(input('Digite um número para calcular o fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

from time import sleep
n = int(input('Digite um número para o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
sleep(1)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

