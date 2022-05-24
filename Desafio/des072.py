# Crie uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numTec = int(input('Digite um número de zero a vinte: '))
while True:
    if 0 <= numTec <= 20:
        break
    else:
        numTec = int(input("Valor inválido. Digite novamente: "))
for i in range(len(contagem)):
    if i == numTec:
        print(f'Você escolheu o número {contagem[i]}')
