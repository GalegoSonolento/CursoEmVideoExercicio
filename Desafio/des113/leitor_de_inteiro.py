# def leiaInt(txt):
#     new_input = str(input(txt))
#     while not new_input.isnumeric():
#         print('\033[0;31m ERRO! Digite apenas um número!\033[38m')
#         new_input = str(input(txt))
#     return new_input


def leiaInt(num):
    try:
        int(num)
        print('Trocado')
    except:
        print('ERRO: por favor, digite um número inteiro válido')
        return -1
    else:
        print('Sucesso')
        return num
