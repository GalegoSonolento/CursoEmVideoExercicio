# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
n1 = str(input('\033[31m Primeiro trab: '))
n2 = str(input('\033[32m Segundo trab: '))
n3 = str(input('\033[33m Terceiro Trab: '))
n4 = str(input('\033[34m Quarto trab: '))
trabs = [n1, n2, n3, n4]
ordem = random.sample(trabs, k=len(trabs))
print('\033[1;35m', ordem)
