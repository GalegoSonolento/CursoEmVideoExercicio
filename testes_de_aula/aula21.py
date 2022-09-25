# print("Olá Mundo")
# help(print)
#
# print("=-"*30)
#
# print(input.__doc__)
# help(input)

# from time import sleep # Importação de função "desconhecida"
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('FIM!')
#
#
# contador(2, 10, 2)
# help(contador)
# print(contador.__doc__)


# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# somar(3, 2, 5)
# somar(8, 4)
# somar(b=3, c=1)


# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'na função teste, o x vale {x}')
#
#
# # Programa principal
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}')


def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')


n1 = 2
print(f'n1 global vale {n1}')
funcao()






