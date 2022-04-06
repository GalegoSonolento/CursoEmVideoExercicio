# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valo
# da casa, o salário do comprador, e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
print('Esse programa validará ou não a compra da casa. Pro favor, responda as perguntas abaixo: ')
valorCasa = float(input('Digite o valor do imóvel: '))
salarioCompr = float(input('Digite seu salário: '))
prest = float(input('Digite em quantos anos a casa será paga: '))
meses = prest * 12
prest = valorCasa / meses
if prest < (salarioCompr * 0.3):
    print('Seu empréstimo foi aprovado')
else:
    print('Seu empréstimo foi reprovado')
