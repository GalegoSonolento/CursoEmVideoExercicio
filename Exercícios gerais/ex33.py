a = float(input('Digite um número: '))
b = float(input('Digite outro: '))
c = float(input('Digite outro: '))
menor = a
if b<a and c<a:
    menor = b
elif c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
elif c>a and c>b:
    maior = c
print(menor)
print(maior)