# # FAça um programa que leia o sexo de uma pessoa, mas só aeite "M" ou "F"
# # Caso esteja errado, peça a digitação novamente até ter um valor correto
#
# sexo = str(input('Digite seu sexo: '))
# while sexo != 'M' and sexo != 'F':
#     sexo = str(input('Sexo inválido, digite novamente: '))

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
# idade = int(input('Informe sua idade: '))
# print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo resgistrado com sucesso'.format(sexo))
