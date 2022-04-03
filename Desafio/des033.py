# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
n1 = float(input('\033[31m Digite um número: '))
n2 = float(input('\033[32m Digite outro: '))
n3 = float(input('\033[33m Digite outro: '))
if n1 < n2 and n1 < n3:
    print('\033[34m {} é o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('\033[35m {} é o menor'.format(n2))
else:
    print('\033[36m {} é o menor'.format(n3))
