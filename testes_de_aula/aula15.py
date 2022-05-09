# cont = 1
# while True:
#     print(cont, '...', end='')
#     cont += 1
# print('Acabou')

# n = cont = 0
# while cont < 3:
#     n = int(input('Digite um número: '))
#     cont += 1

# n = s = 0
# while n != 999:
#     n = int(input('Digite um número: '))
#     s += n
# print('A soma vale {}'.format(s))

# s = n = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# # print('A soma vale {}'.format(s))
# print(f'A soma vale {s}')

nome = 'Jpsé'
idade = 33
salario = 987.63
# print(f'O {nome} tem {idade} anos.')
# print('O {} tem {} anos'.format(nome, idade))
print(f'O {nome:->20} tem {idade} e ganha R${salario:.2f}')