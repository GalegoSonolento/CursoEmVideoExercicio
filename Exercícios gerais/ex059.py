# # Crie um programa que leia dois valores e mostre um menu na tela:
# # [1] somar
# # [2] multiplicar
# # [3] maior
# # [4] novos números
# # [5] sair do programa
# # Seu programa deverá realizar a operação solicitada em cada caso
# num1 = float(input('Digite um valor para cálculo: '))
# num2 = float(input('Digite outro: '))
# while True:
#     print('''Escolha entre as opções abaixo:
#     [1] somar
#     [2] multiplicar
#     [3] maior
#     [4] novos números
#     [5] sair do programa''')
#     opcao = int(input('Digite o número da operação que deseja: '))
#     if opcao == 1:
#         soma = num1 + num2
#         print('A soma dos números {} e {} é: {}'.format(num1, num2, soma))
#         break
#     elif opcao == 2:
#         multiplicacao = num1 * num2
#         print('A multiplicação entre {} e {} é {}'.format(num1, num2, multiplicacao))
#         break
#     elif opcao == 3:
#         if num1 > num2:
#             print('{} é maior que {}'.format(num1, num2))
#             break
#         elif num1 < num2:
#             print('{} é maior que {}'.format(num2, num1))
#             break
#     elif opcao == 4:
#         print('Digite novos números: ')
#         num1 = float(input('Digite um novo número: '))
#         num2 = float(input('Digite um novo número: '))
#     elif opcao == 5:
#         print('Obrigado por utilizar o programa')
#         break

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''Escolha entre as opções abaixo:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação de {} por {} é {}'.format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        n1 = int(input('Digite o novo valor: '))
        n2 = int(input('Digite o novo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. TEnte novamente')
    print('==-==-==-==-==')
    sleep(2)
print('Fim do programa')
