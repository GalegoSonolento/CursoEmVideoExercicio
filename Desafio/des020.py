# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
n1 = str(input('Primeiro trab: '))
n2 = str(input('Segundo trab: '))
n3 = str(input('Terceiro Trab: '))
n4 = str(input('Quarto trab: '))
trabs = [n1, n2, n3, n4]
ordem = random.sample(trabs, k=len(trabs))
print(ordem)
