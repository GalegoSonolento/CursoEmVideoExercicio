# numDig = 0
# lista = []
# num5 = False
# while True:
#     num = int(input("Digite um valor: "))
#     if num == 5:
#         num5 = True
#     numDig += 1
#     lista.append(num)
#     resp = str(input('Você quer continuar? [S/N] ')).lower().strip()
#     if resp == 'n':
#         break
# a = lista.sort(reverse=True)
# print('-=' * 30)
# print(f'Você digitou {numDig} números.')
# print(f'A lista em ordem decrescnete deles é: {sorted(lista, reverse=True)}')
# print('O número 5 está na lista!' if num5 else 'O número 5 não está na lista!')

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} valores.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
