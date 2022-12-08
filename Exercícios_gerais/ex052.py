num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(i), end='')
print('\nO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele NÃO é primo')