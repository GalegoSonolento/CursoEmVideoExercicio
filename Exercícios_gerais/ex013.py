salario = float(input('Qual é seu salário? R$'))
novo = salario + (salario * 15 / 100)
print('O novo salário, a partir de R${:.2f}, fica R${:.2f}'.format(salario, novo))