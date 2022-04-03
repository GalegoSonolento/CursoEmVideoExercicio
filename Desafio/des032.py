# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('\033[4;30;43m Insira um ano aqui: \033[m'))
if ano % 4 == 0:
    print('\033[7;35m Seu ano é bissexto')
else:
    print('\033[1;36m Seu ano é normal')
