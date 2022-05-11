# cont = 0
# soma = 0
# while True:
#     num = int(input('Digite um número inteiro [ou 999 para parar]: '))
#     if num != 999:
#         cont += 1
#         soma += num
#     else:
#         break
# print(f'Foram digitados {cont} números, com soma de {soma}.')

soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores é {soma} com {cont} valores digitados!')
