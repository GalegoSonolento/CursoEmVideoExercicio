# import random
# maior = menor = 0
# multiplicador = 100
# teste = [int(random.random() * multiplicador), int(random.random() * multiplicador), int(random.random() * multiplicador), int(random.random() * multiplicador), int(random.random() * multiplicador)]
# for i in range(len(teste)):
#     print(f'- {teste[i]}', end=' ')
#     print(' ')
#     if i == 0:
#         maior = menor = teste[i]
#     else:
#         if maior < teste[i]:
#             maior = teste[i]
#         if menor > teste[i]:
#             menor = teste[i]
# print(f'O menor valor é {menor} e o maior é {maior}')

from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for i in tupla:
    print(f'{i}', end=' ')
print(f'\nO maior sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
