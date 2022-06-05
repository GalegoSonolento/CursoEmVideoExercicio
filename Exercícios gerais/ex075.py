# surge9 = 0
# pos3 = ''
# numPares = ''
# tupla = (int(input("Digite um valor para a tupla: ")), int(input("Digite outro valor para a tupla: ")),
#          int(input("Digite outro valor para a tupla: ")), int(input("Digite outro valor para a tupla: ")),
#          int(input("Digite outro valor para a tupla: ")), int(input("Digite outro valor para a tupla: ")))
# for i in range(len(tupla)):
#     if tupla[i] == 9:
#         surge9 += 1
#     elif tupla[i] == 3:
#         pos3 += f'{i}, ' if i < len(tupla)-1 else f'{i}.'
#     elif tupla[i] % 2 == 0:
#         numPares += f'{tupla[i]}, ' if i < len(tupla)-1 else f'{tupla[i]}.'
# print(f'Apareceram {surge9} números 9')
# print(f'O número 3 está nas posições {pos3}')
# print(f'Os números pares são {numPares}')

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
       print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end=' ')
for i in num:
       if i % 2 == 0:
              print(i, end=' ')
