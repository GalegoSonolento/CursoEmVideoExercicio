# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    pares.append(num) if num % 2 == 0 else impares.append(num)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Os números digitados foram: {valores}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
