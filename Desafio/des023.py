# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# separar dezenas, centenas, etc...
num = int(input('\033[31m Digite um número inteiro: '))
if num < 0 or num > 9999:
    print('\033[32m Erro, reinicie o sistema')
else:
    milhares = num // 1000
    centenas = num // 100
    dezenas = num // 10
    unidades = num // 1
    print('\033[33m O número possui {} unidades'.format(unidades))
    print('\033[34m {} dezenas'.format(dezenas))
    print('\033[35m {} centenas'.format(centenas))
    print('\033[36m E {} milhares'.format(milhares))
