# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

n = input('\033[32m Digite algo: ')

if n.isnumeric():
    print('\033[31m número')
elif n.isalpha():
    if n.isupper():
        print('\033[33m letra maiúscula')
    elif n.islower():
        print('\033[35m letra minúscula')
elif n.isalnum():
    print('\033[36m alfanumérico')