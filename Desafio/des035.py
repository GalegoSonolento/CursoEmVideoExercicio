# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas formam ou não um triângulo
a = float(input('Digite um valor para um lado do triângulo: '))
b = float(input('Digite outro: '))
c = float(input('Digite outro: '))
if abs(b-c) < a < (b+c) or abs(a-c)<b<(a+c) or abs(a-b)<c<(a+b):
    print('Você tem um triânguo possível')
else:
    print('Você não tem um triângulo')
