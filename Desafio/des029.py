# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite
vel = float(input('\033[1;35m Qual era a velocidade do carro? '))
if vel > 80:
    print('\033[32m O motorista deve ser multado')
    print('\033[36m A multa custará {} pelo excesso de velocidade'.format((vel - 80) * 7))
else:
    print('\033[37m Está tudo certo, sem multa')
