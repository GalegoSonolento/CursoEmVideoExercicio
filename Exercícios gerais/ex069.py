# from time import sleep
# quantM18 = manos = minasUnder20 = 0
# while True:
#     while True:
#         idade = int(input('Digite a idade da pessoa: '))
#         if idade > 0:
#             break
#     while True:
#         sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
#         if sexo in 'FM':
#             break
#     if idade < 18:
#         quantM18 += 1
#     if sexo == 'M':
#         manos += 1
#     if sexo == 'F' and idade < 20:
#         minasUnder20 += 1
#     opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
#     if opcao == 'N':
#         break
#     elif opcao == 'S':
#         print('Continuando...')
#         sleep(1)
# print(f'Foram cadastrados {quantM18} menores de 18 anos, {manos} homens e {minasUnder20}')

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou')
print(f'Temos {tot18} maiores de 18 anos, {totH} homens e {totM20} mulheres com menos de 20 anos.')
