# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
# Precisa fazer um loop pro jogo sempre funcionar

import random
from time import sleep
vitorias = 0
print('='*30)
print('JOGUE PAR OU ÍMPAR COM A MÁQUINA!')
print('='*30)
while True:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    escolhaPC = random.choice(nums)
    numP = int(input('Diga um número de 1 a 10 para jogar: '))
    opcao = str(input('Você escolhe par ou ímpar [P/I]? ')).strip().upper()[0]
    print('Processando...')
    sleep(1)
    soma = escolhaPC + numP
    print(f'A máquina escolheu {escolhaPC} e você {numP}. A soma foi {soma}')
    if opcao == 'P' and soma % 2 == 0:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        sleep(1)
        print('-='*30)
        vitorias += 1
    elif opcao == 'P' and soma % 2 != 0:
        print('VOCÊ PERDEU!')
        print('-=' * 30)
        break
    elif opcao == 'I' and soma % 2 != 0:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        sleep(1)
        print('-=' * 30)
        vitorias += 1
    elif opcao == 'I' and soma % 2 == 0:
        print('VOCÊ PERDEU!')
        print('-=' * 30)
        break
print(f'Jogo finalizado, você obteve {vitorias} vitórias!')
