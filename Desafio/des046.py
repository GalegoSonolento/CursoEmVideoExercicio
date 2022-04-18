# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10
# até o, com uma pausa de 1 segundo entre eles.
import time
import emoji
print('CONTAGEM REGRESSIVA PARA OS FOGOS!')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print()

