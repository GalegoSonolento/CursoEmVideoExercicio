# # Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# # Caso o número já exista lá dentro, ele não será adicionado.
# # No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
#
# lista = []
# duplicado = False
# while True:
#     num = int(input('Digite um valor a ser adicionado: '))
#     for i in lista:
#         if num == i:
#             duplicado = True
#     if duplicado:
#         print('Valor duplicado! Não vou adicionar...')
#     else:
#         lista.append(num)
#         print('Valor adicionado com sucesso...')
#     sn = str(input('Deseja continuar? [S/N]')).upper()
#     if sn == 'N':
#         break
# print('='*30)
# lista.sort()
# print('Você adicionou os valores ', end='')
# print(lista)

nums = []
while True:
    n = int(input('Digite um valor: '))
    if n not in nums:
        nums.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'nN':
        break
print('-='*30)
nums.sort()
print(f'Você digitou os valores {nums}')
