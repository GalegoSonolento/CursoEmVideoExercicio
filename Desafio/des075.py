# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o valor 3.
# c) Quais foram os números pares

surge9 = 0
pos3 = ''
numPares = ''
tupla = (int(input("Digite um valor para a tupla: ")), int(input("Digite outro valor para a tupla: ")),
         int(input("Digite outro valor para a tupla: ")), int(input("Digite outro valor para a tupla: ")),
         int(input("Digite outro valor para a tupla: ")), int(input("Digite outro valor para a tupla: ")))
for i in range(len(tupla)):
    if tupla[i] == 9:
        surge9 += 1
    elif tupla[i] == 3:
        pos3 += f'{i}, ' if i < len(tupla)-1 else f'{i}.'
    elif tupla[i] % 2 == 0:
        numPares += f'{tupla[i]}, ' if i < len(tupla)-1 else f'{tupla[i]}.'
print(f'Apareceram {surge9} números 9')
print(f'O número 3 está nas posições {pos3}')
print(f'Os números pares são {numPares}')
