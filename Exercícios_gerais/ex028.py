from random import randint
from time import sleep
numPC = randint(0, 5) # Faz o pc sortear
print('-=-' * 20)
numUS = int(input('Escolha um número de 0 a 5 e tente acertar o que a máquina escolheu: '))
print('-=-' * 20)
print('Processando...')
sleep(3)
if numPC == numUS:
    print('Você acertou')
else:
    print('Você errou')
    print('Pensei no {}'.format(numPC))
