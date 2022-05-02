# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
num1 = float(input('Digite um valor para cálculo: '))
num2 = float(input('Digite outro: '))
while True:
    print('''Escolha entre as opções abaixo:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Digite o número da operação que deseja: '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma dos números {} e {} é: {}'.format(num1, num2, soma))
        break
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, multiplicacao))
        break
    elif opcao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
            break
        elif num1 < num2:
            print('{} é maior que {}'.format(num2, num1))
            break
    elif opcao == 4:
        print('Digite novos números: ')
        num1 = float(input('Digite um novo número: '))
        num2 = float(input('Digite um novo número: '))
    elif opcao == 5:
        print('Obrigado por utilizar o programa')
        break
