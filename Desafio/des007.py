# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
# a sua média

nt1 = float(input('\033[31m Digite sua priemira nota: '))
nt2 = float(input('\033[32m Digite sua segunda nota: '))

print('\033[34m Sua média é {:.1f}.'.format((nt1+nt2)/2))