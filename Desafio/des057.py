# FAça um programa que leia o sexo de uma pessoa, mas só aeite "M" ou "F"
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('Digite seu sexo: '))
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo inválido, digite novamente: '))
