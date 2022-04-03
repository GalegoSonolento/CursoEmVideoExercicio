# Crie um programa que leia um número inteiro qualquer e mostre na tela se é par ou ímpar
n = int(input('\033[31m Digite um número inteiro: '))
if n % 2 == 0:
    print('\033[32m Seu númro é par')
else:
    print('\033[33m Seu número é ímpar')
