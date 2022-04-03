# Faça um algoritimo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento

salario = float(input('\033[31m Digite seu salário: '))

aumento = salario*0.15

print('\033[32m seu salário com aumento é: {}'.format(salario+aumento))