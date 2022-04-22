# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão
a1 = int(input('Diga o primeiro termo de uma PA: '))
r = int(input('Diga a razão da PA: '))
if a1 == r:
    for i in range(a1, r * 11, r):
        print(i)
else:
    for j in range(a1, r * 10, r):
        print(j)
