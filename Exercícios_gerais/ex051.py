a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
a10 = a1 + (10 - 1) * razao
for i in range(a1, a10 + razao, razao):
    print('{}'.format(i), end=' -> ')
print('Acabou')