# Faça um programa que calcule a soma de todos os número ímpares que são múltiplos de 3 e que se encontram no intervalo
# de 1 até 500
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
