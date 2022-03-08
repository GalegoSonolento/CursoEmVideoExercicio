# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

n = input('Digite algo: ')

if n.isnumeric():
    print('número')
elif n.isalpha():
    if n.isupper():
        print('letra maiúscula')
    elif n.islower():
        print('letra minúscula')
elif n.isalnum():
    print('alfanumérico')