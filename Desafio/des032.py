# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Insira um ano aqui: '))
if ano % 4 == 0:
    print('Seu ano é bissexto')
else:
    print('Seu ano é normal')
