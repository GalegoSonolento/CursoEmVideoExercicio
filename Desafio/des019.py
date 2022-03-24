# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome escolhido

import random
nom1 = input('Digite o nome do aluno: ')
nom2 = input('Digite o nome de outro: ')
nom3 = input('Digite o nome de outro: ')
nom4 = input('Digite o nome de outro: ')
print(random.choice([nom1, nom2, nom3, nom4]))

