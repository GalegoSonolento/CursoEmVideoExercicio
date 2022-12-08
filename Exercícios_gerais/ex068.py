# import random
# from time import sleep
# vitorias = 0
# print('='*30)
# print('JOGUE PAR OU ÍMPAR COM A MÁQUINA!')
# print('='*30)
# while True:
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     escolhaPC = random.choice(nums)
#     numP = int(input('Diga um número de 1 a 10 para jogar: '))
#     opcao = str(input('Você escolhe par ou ímpar [P/I]? ')).strip().upper()[0]
#     print('Processando...')
#     sleep(1)
#     soma = escolhaPC + numP
#     print(f'A máquina escolheu {escolhaPC} e você {numP}. A soma foi {soma}')
#     if opcao == 'P' and soma % 2 == 0:
#         print('VOCÊ VENCEU!')
#         print('Vamos jogar novamente...')
#         sleep(1)
#         print('-='*30)
#         vitorias += 1
#     elif opcao == 'P' and soma % 2 != 0:
#         print('VOCÊ PERDEU!')
#         print('-=' * 30)
#         break
#     elif opcao == 'I' and soma % 2 != 0:
#         print('VOCÊ VENCEU!')
#         print('Vamos jogar novamente...')
#         sleep(1)
#         print('-=' * 30)
#         vitorias += 1
#     elif opcao == 'I' and soma % 2 == 0:
#         print('VOCÊ PERDEU!')
#         print('-=' * 30)
#         break
# print(f'Jogo finalizado, você obteve {vitorias} vitórias!')

from random import randint
vitoria = 0
while True:
    player = int(input("Digite um valor: "))
    comp = randint(0, 10)
    total = player + comp
    tipo = " "
    while tipo not in 'PpIi':
        tipo = str(input("Par ou ímpar [P/I]? ")).strip().upper()[0]
    print(f"Você jogou {player} e o computador {comp}, o total é {total}")
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
print(f'Você ganhou {vitoria} vezes')
