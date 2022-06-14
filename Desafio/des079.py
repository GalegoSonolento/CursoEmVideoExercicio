# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
duplicado = False
while True:
    num = int(input('Digite um valor a ser adicionado: '))
    for i in lista:
        if num == i:
            duplicado = True
    if duplicado:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    sn = str(input('Deseja continuar? [S/N]')).upper()
    if sn == 'N':
        break
print('='*30)
lista.sort()
print('Você adicionou os valores ', end='')
print(lista)
