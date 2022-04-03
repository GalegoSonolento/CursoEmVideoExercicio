# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome escolhido

import random
nom1 = input('\033[31m Digite o nome do aluno: ')
nom2 = input('\033[32m Digite o nome de outro: ')
nom3 = input('\033[33m Digite o nome de outro: ')
nom4 = input('\033[34m Digite o nome de outro: ')
print('\033[1;35m', random.choice([nom1, nom2, nom3, nom4]))

