# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# separar dezenas, centenas, etc...
num = int(input('Digite um número inteiro: '))
if num < 0 or num > 9999:
    print('Erro, reinicie o sistema')
else:
    milhares = num // 1000
    centenas = num // 100
    dezenas = num // 10
    unidades = num // 1
    print('O número possui {} unidades'.format(unidades))
    print('{} dezenas'.format(dezenas))
    print('{} centenas'.format(centenas))
    print('E {} milhares'.format(milhares))
