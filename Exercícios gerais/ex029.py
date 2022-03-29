vel = float(input('Qual era a velocidade do carro? '))
if vel > 80:
    print('O motorista deve ser multado por exceder o limite de 80km/h')
    print('A multa custará {:.2f} pelo excesso de velocidade'.format((vel - 80) * 7))

print('Tenha um bom dia, dirija com segurança.')
