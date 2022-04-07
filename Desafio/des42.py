# Refaça o desafio 35 dos triângulos, acrescntando o recurso de mostrar que tipo de triângulo será formado
#- equilátero: todos os lados iguais
#Isóceles: dois lados iguais
#- Escaleno: todos os lados diferentes
a = float(input('\033[31m Digite um valor para um lado do triângulo: '))
b = float(input('\033[32m Digite outro: '))
c = float(input('\033[33m Digite outro: '))
if abs(b-c) < a < (b+c) or abs(a-c)<b<(a+c) or abs(a-b)<c<(a+b):
    print('\033[34m Você tem um triânguo possível')
    if a == b and a == c and b == c:
        print('Seu triângulo é equilátero')
    elif a != b and a != c and b != c:
        print('Seu triângulo é escaleno')
    else:
        print('Seu triângulo é isóceles')
else:
    print('\033[35m Você não tem um triângulo')
