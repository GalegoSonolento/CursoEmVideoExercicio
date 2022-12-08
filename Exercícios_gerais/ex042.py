a = float(input('\033[31m Digite um valor para um lado do triângulo: '))
b = float(input('\033[32m Digite outro: '))
c = float(input('\033[33m Digite outro: '))
if abs(b-c) < a < (b+c) or abs(a-c)<b<(a+c) or abs(a-b)<c<(a+b):
    print('\033[34m Você tem um triânguo possível - ', end='')
    if a == b == c:
        print('Seu triângulo é equilátero')
    elif a != b != c and a != c:
        print('Seu triângulo é escaleno')
    else:
        print('Seu triângulo é isóceles')
else:
    print('\033[35m Você não tem um triângulo')