# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250.00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite aqui seu salário: '))
if salario <= 1250.00:
    print('Seu reajuste é de 15%, portanto, seu novo salário é de {}'.format(salario + (salario * 0.15)))
else:
    print('Seu reajuste é de 10%, portanto, seu novo salário é {}'.format(salario + (salario * 0.10)))
