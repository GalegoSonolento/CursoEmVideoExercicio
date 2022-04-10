# Crie um programa que faça o computador jogar jokenpô com você (pedra, papel, tesoura)
import random
import time
jokenpo = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('-=' * 12)
print('\033[31m JOGUE JOKENPÔ COM A MÁQUINA!\033[m')
print('-=' * 12)
print('\033[32m ESOLHA UMA DENTRE AS OPÇÕES ABAIXO:'
      '\n -1- Pedra'
      '\n -2- Papel'
      '\n -3- Tesoura\033[m')
opcao = int(input('Digite aqui: '))
print('Processando...')
time.sleep(3)
print('\033[1;35m-_'*12)
if opcao == 1:
    if jokenpo == 'Pedra':
        print('\033[1;35m VOCÊ EMPATOU COM A MÁQUINA!')
    elif jokenpo == 'Papel':
        print('\033[1;35mVOCÊ PERDEU PARA A MÁQUINA!')
    elif jokenpo == 'Tesoura':
        print('\033[1;35mVOCÊ GANHOU DA MÁQUINA!')
elif opcao == 2:
    if jokenpo == 'Pedra':
        print('\033[1;35mVOCÊ VENCEU A MÁQUINA!')
    elif jokenpo == 'Papel':
        print('\033[1;35mVOCÊ EMPATOU COM A MÁQUINA!')
    elif jokenpo == 'Tesoura':
        print('\033[1;35mVOCÊ PERDEU PARA A MÁQUINA!')
elif opcao == 3:
    if jokenpo == 'Pedra':
        print('\033[1;35mVOCÊ PERDEU PARA A MÁQUINA!')
    elif jokenpo == 'Papel':
        print('\033[1;35mVOCÊ GANHOU DA MÁQUINA!')
    elif jokenpo == 'Tesoura':
        print('\033[1;35mVOCÊ EMPATOU COM A MÁQUINA!')
print('-_'*12)
