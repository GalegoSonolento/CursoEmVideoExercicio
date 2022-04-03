# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
nums = [0, 1, 2, 3, 4, 5]
numPC = random.choice(nums)
numUS = int(input('\033[32m Escolha um número de 0 a 5 e tente acertar o que a máquina escolheu: '))
if numPC == numUS:
    print('\033[34m Você acertou')
else:
    print('\033[35m Você errou')
