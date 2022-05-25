# contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
#             'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# numTec = int(input('Digite um número de zero a vinte: '))
# while True:
#     if 0 <= numTec <= 20:
#         break
#     else:
#         numTec = int(input("Valor inválido. Digite novamente: "))
# for i in range(len(contagem)):
#     if i == numTec:
#         print(f'Você escolheu o número {contagem[i]}')

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente', end=' ')
    print(f'Você digitou o número {cont[num]}')
    while True:
        opcao = str(input('Deseja pergunar novamente? [S/N]')).strip().upper()[0]
        if opcao not in 'SN':
            print('Opção inválida.', end=' ')
        else:
            break;
    if opcao == 'N':
        break
print('Obrigado por utilizar o programa')
