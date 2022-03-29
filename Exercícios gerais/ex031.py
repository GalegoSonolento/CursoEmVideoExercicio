dist = float(input('Qual a distância da viagem (em quilômetros)? '))
'''if dist <= 200:
    print('Sua passagem custará {:.2f} reais'.format(dist * 0.5))
elif dist > 200:
    print('Sua passagem custará {:.2f} reais'.format(dist * 0.45))'''

preco = dist * 0.5 if dist <= 200 else dist * 0.45
print(preco)
