# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas formam ou não um triângulo
a = float(input('\033[31m Digite um valor para um lado do triângulo: '))
b = float(input('\033[32m Digite outro: '))
c = float(input('\033[33m Digite outro: '))
if abs(b-c) < a < (b+c) or abs(a-c)<b<(a+c) or abs(a-b)<c<(a+b):
    print('\033[34m Você tem um triânguo possível')
else:
    print('\033[35m Você não tem um triângulo')
