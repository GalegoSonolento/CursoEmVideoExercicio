# Desenvolva um programa qu pergunta a distância de uma viagem em
# calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,40 para viagens mais longas
dist = float(input('\033[4;31;47m Qual a distância da viagem (em quilômetros)? \033[m'))
if dist <= 200:
    print('\033[32m Sua passagem custará {} reais'.format(dist * 0.5))
elif dist > 200:
    print('\033[34m Sua passagem custará {} reais'.format(dist * 0.4))
