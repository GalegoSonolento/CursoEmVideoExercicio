# cont = 1
# while True:
#     num = int(input('Digite um número para mostrar a tabuada [digite um negativo para finalizar o programa]: '))
#     if num <= 0:
#         break
#     print('='*12)
#     print(f'Tabuada do {num}:')
#     while True:
#         if cont == 11:
#             break
#         espaco = ' x' if cont < 10 else 'x'
#         print(f'{cont: < 2} {espaco} {num} = {num * cont}')
#         cont += 1
#     print('='*12)
#     cont = 1
# print('Obrigado por utilizar o programa!')

while True:
    num = int(input('Quer ler a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-'*30)
print('Programa tabuada encerrado')