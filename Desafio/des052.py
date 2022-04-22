# Faça um programa que leia um número inteiro e diga se ela é ou não um número primo
num = int(input('Digite um número para verificar se ele é ou não primo: '))
isPrimo = True
for i in range(2, num):
    if num % i == 0:
        isPrimo = False
if isPrimo:
    print('O número é primo')
else:
    print('O número não é primo')
