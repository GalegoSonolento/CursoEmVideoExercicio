# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro: '))
n3 = float(input('Digite outro: '))
if n1 < n2 and n1 < n3:
    print('{} é o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} é o menor'.format(n2))
else:
    print('{} é o menor'.format(n3))
