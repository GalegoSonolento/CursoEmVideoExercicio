# Faça um programa que leia uma frase no teclado e mostre:
# Quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
frase = str(input('\033[31m Digite uma pequena frase: ')).strip().lower()
print('\033[32m Na sua frase, a letra \'a\' aparece {} vezes'.format(frase.count('a')))
print('\033[33m A letra \'a\' aparece pela primeira vez na posição {}'.format(frase.find('a')))
ultimo = frase.rfind('a')
print('\033[1;34m', ultimo)
