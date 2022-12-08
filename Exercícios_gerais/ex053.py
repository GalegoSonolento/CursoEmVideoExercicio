frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# print('Você digitou a frase {}'.format(junto))
# inverso = ''
inverso = junto[::-1]
'''for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
# print(junto, inverso)'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')