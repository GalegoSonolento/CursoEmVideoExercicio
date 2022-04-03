# faça um programa que leia um número inteiro e mostre na tela o seu sucessor
# e seu antecessor

num = float(input('\033[31m Digite um número qualquer na tela: '))

print('\033[32m Você digitou {}'.format(num))
print('\033[33m O antecessor é {}.'.format(num-1))
print('\033[34m O sucessor é {}.'.format(num+1))