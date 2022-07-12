# valores = []
# pares = []
# impares = []
# while True:
#     num = int(input('Digite um valor: '))
#     valores.append(num)
#     pares.append(num) if num % 2 == 0 else impares.append(num)
#     resp = str(input('Deseja continuar? [S/N] '))
#     if resp in 'nN':
#         break
# print('-=' * 30)
# print(f'Os números digitados foram: {valores}')
# print(f'Os números pares são: {pares}')
# print(f'Os números ímpares são: {impares}')

num = []
pares = list()
impares = list()
while True:
    num.append(int(input("Digite um número: ")))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('-=' * 30)
print(f'A lista completa é: {num}')
print(f'Os pares são {pares}')
print(f'Os ímpares são {impares}')
