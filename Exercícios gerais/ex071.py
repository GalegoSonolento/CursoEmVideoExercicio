# nota50 = nota20 = nota10 = nota1 = saque = 0
# while True:
#     valor = int(input("Digite o valor a ser sacado [apenas números inteiros]: "))
#     saque = valor
#     if valor <= 0:
#         print("Você não pode sacar valores negativos!")
#     else:
#         break
# while True:
#     if valor >= 50:
#         valor -= 50
#         nota50 += 1
#     elif valor >= 20:
#         valor -= 20
#         nota20 += 1
#     elif valor >= 10:
#         valor -= 10
#         nota10 += 1
#     elif valor >= 1:
#         valor -= 1
#         nota1 += 1
#     else:
#         break
# print(f"Seu saque de {saque} reais virá com {nota50} notas de 50, {nota20} notas de 20, {nota10} notas de 10 e
# {nota1} "
#       f"notas de 1")

print('='*40)
print('{:^30}'.format('BANCÃO DUS GURI'))
print('='*40)
valor = int(input('Que valor você quer sacar? '))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('='*30)
print('{:^30}'.format('Volte sempre!'))