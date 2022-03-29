# Desenvolva um programa qu pergunta a distância de uma viagem em
# calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,40 para viagens mais longas
dist = float(input('Qual a distância da viagem (em quilômetros)? '))
if dist <= 200:
    print('Sua passagem custará {} reais'.format(dist * 0.5))
elif dist > 200:
    print('Sua passagem custará {} reais'.format(dist * 0.4))
