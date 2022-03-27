# Faça um programa que leia uma frase no teclado e mostre:
# Quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
frase = str(input('Digite uma pequena frase: ')).strip().lower()
print('Na sua frase, a letra \'a\' aparece {} vezes'.format(frase.count('a')))
print('A letra \'a\' aparece pela primeira vez na posição {}'.format(frase.find('a')))
ultimo = frase.rfind('a')
print(ultimo)
