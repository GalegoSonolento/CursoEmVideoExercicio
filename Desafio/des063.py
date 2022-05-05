# Escreve um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos e uma sequência
# de fibonacci
#Ex: 0 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Digite quantos números da sequência de Fibonatti desejas ver: '))
cont = 0
p1 = 0
p2 = 1
while cont < n:
    if cont == 0:
        print('{} - '.format(p1), end='')
        print('{} - '.format(p2), end='')
        cont += 2
    else:
        p1 = p1 + p2
        print('{} - '.format(p1), end='')
        p2 = p2 + p1
        print('{} - '.format(p2), end='')
        cont += 2
print('Fim da sequência solicitada')

