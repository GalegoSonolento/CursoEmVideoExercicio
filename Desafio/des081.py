# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numDig = 0
lista = []
num5 = False
while True:
    num = int(input("Digite um valor: "))
    if num == 5:
        num5 = True
    numDig += 1
    lista.append(num)
    resp = str(input('Você quer continuar? [S/N] ')).lower().strip()
    if resp == 'n':
        break
a = lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {numDig} números.')
print(f'A lista em ordem decrescnete deles é: {sorted(lista, reverse=True)}')
print('O número 5 está na lista!' if num5 else 'O número 5 não está na lista!')
