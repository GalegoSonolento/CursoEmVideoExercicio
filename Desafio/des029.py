# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite
vel = float(input('Qual era a velocidade do carro? '))
if vel > 80:
    print('O motorista deve ser multado')
    print('A multa custará {} pelo excesso de velocidade'.format((vel - 80) * 7))
else:
    print('Está tudo certo, sem multa')
