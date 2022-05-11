# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo
# Tem que por em um while e fazer o código de tabuada repetir

cont = 1
while True:
    num = int(input('Digite um número para mostrar a tabuada [digite um negativo para finalizar o programa]: '))
    if num <= 0:
        break
    print('='*12)
    print(f'Tabuada do {num}:')
    while True:
        if cont == 11:
            break
        espaco = ' x' if cont < 10 else 'x'
        print(f'{cont: < 2} {espaco} {num} = {num * cont}')
        cont += 1
    print('='*12)
    cont = 1
print('Obrigado por utilizar o programa!')
