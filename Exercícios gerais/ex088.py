from time import sleep
from random import randint    # Randomizador de números inteiros do python. Diferentemente do Java, o Python já tem um randomizador próprio, sem a necessidade de criar uma linha tal qual em java (Maatn)

lista = list()
jogos = list()      # Lista para guardar os jogos (compostas de outras listas)
print('-=' * 30)
print('     JOGA NA MEGA SENA     ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1    # Limita a quantidade de repetições do while
while tot <= quant:
  cont = 0
  while True:
    num = randint(1, 60)    # A função de radint facilita o trabalho e economiza umas 4 linhas
    if num not in lista:    # A possibilidade de usar "not in" alguma coisa também economiza algumas linhas - python possui espeficidades a mais q java
      lista.append(num)
      cont += 1
    if cont == 6:
      break
  lista.sort()
  jogos.append(lista[:])    # Append com a cópia da lista usada para guardar os sorteios do computador
  lista.clear()    # Apaga a lista
  tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)  # Finaliza o sorteio de um dos grupos da sena
for i, j in enumerate(jogos):
  print(f'Jogo {i+1}: {j}')
  sleep(1)
print('-=' * 3, '<BOA SORTE!>', '-=' * 3)