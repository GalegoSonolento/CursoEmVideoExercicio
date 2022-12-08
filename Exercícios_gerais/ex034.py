salario = float(input('Digite aqui seu salário: '))
if salario <= 1250.00:
    print('Seu reajuste é de 15%, portanto, seu novo salário é de {}'.format(salario + (salario * 0.15)))
else:
    print('Seu reajuste é de 10%, portanto, seu novo salário é {}'.format(salario + (salario * 0.10)))