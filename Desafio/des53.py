# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#Ex: apos a sopa
#A sacada da casa
#o lobo ama o bolo
# anotaram a data da maratona
#Desconsiderar espaços e acentos
import unidecode
termoCAssento = str(input('Digite uma tentativa de palíndromo: ')).lower().strip().replace(' ', '')
termo = unidecode.unidecode(termoCAssento)
# print(termo)
termoInvertido = ''.join(reversed(termo))
# print(termo)
cont = 0
for i in range(len(termo)):
    # print('\033[35m', i, '\033[m')
    for j in range(len(termoInvertido)):
        # print('\033[32m', j, '\033[m')
        if i == j:
            letraTermo = termo[i]
            letraInvertida = termoInvertido[j]
            if letraTermo == letraInvertida:
                cont += 1
            break
if cont == len(termo):
    print('É um palíndromo')
else:
    print('não é um palíndromo')


# for k in termo:
#     print(k, end='')
# for i in range(len(termo), 0, -1):
#     print(i)
#     for j in termo:
#         if j == i:
#             cont += 1
# if cont == len(termo):
#     print('É um palíndromo')