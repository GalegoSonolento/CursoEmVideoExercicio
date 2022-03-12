n = int(input('Coloque um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)

# print('Dobro é {}, triplo é {} e a raiz é {}'.format(d, t, r))

print('O dobre de {} \n vale {}'.format(n, d))
print('o triplo de {} \n vale {}'.format(n, t))
print('A raiz de {} \n vale {:.2f}'.format(n, pow(n, (1 / 2))))
