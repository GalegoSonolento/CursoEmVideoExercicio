# Melhore op jogo do desafio 028 onde o computadopr vai pensar em um número entre 0 e 10 Só que agora o jogado r
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import random
cont = 0
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numPC = random.choice(nums)
print(numPC)
while True:
    cont += 1
    numUS = int(input('\033[32m Escolha um número de 0 a 10 e palpite até acertar o que a máquina escolheu: '))
    if numUS == numPC:
        break
print('Você acertou o número que a máquina pensou em {} tentativas'.format(cont))


