# # Crie um programa que leia vários valores inteiros pelo teclado. No final da execução, mostre a média entre todos
# # os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# # continuar a digitar valores.
#
# cont = soma = 0
# num = -1
# maior = 0
# menor = 0
# while num != 0:
#     num = int(input('Digite um número inteiro pelo teclado [0 para parar]: '))
#     if num > 0:
#         soma += num
#         cont += 1
#     if cont == 1:
#         maior = num
#         menor = num
#     elif cont != 0:
#         if num > maior:
#             maior = num
#         elif num < menor and num != 0:
#             menor = num
# media = soma/cont
# print('''O maior número digitado foi {}
#       O menor número digitado foi {}
#       E a média de todos os digitados (sem o zero), é {}'''.format(maior, menor, media))

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
