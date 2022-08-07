# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

import random
from time import sleep

listaMestre = []
listaTemp = []
print('-' * 30)
msg = str('JOGA NA MEGA SENA')
print(f'{msg:^30}')
print('-' * 30)
quantJogs = int(input('Quantos jogos serão sorteados? '))
print('-=' * 3, f'SORTEANDO {quantJogs} JOGOS', '-=' * 3)
for i in range(0, quantJogs):
  cont = 0
  while True:
    num = (int)(random.random() * 60) + 1
    if cont == 0:
      listaTemp.append(num)
      cont += 1
    entraLista = True
    for k in listaTemp:
      if k == num:
        entraLista = False
        break
    if entraLista:
      listaTemp.append(num)
      cont += 1
    if cont == 6:
      listaTemp.sort()
      listaMestre.append(listaTemp[:])
      listaTemp.clear()
      break
for i, j in enumerate(listaMestre):
  print(f'Jogo {i+1}: {j}')
  sleep(1)
print('-=' * 3, '< BOA SORTE! >', '-=' * 3)