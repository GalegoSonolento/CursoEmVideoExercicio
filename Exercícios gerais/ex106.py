# # Exercício Python 106: Faça um mini-sistema que usa o interactive help do python. O usuário vai digitar o comando
# # e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores
#
#
# def titulo(tf='sas', tit=False):
#     if tit:
#         print('\033[42m', '~' * 30, '\n  SISTEMA DE AJUDA PyHELP', '\n', '~' * 30)
#         print('\033[m', end='')
#     elif tf == 'fim':
#         print('\033[41m', '~' * 12, '\n', ' Até Logo! ', '\n', '~' * 12)
#         print('\033[m')
#     else:
#         tamLinha = 28 + len(tf) + 4
#         print('\033[30;44m', '~' * tamLinha, '\n', f' Acessando manual do comando "{tf}"', '\n', '~' * tamLinha)
#         print('\033[m', end='')
#
#
# def funcao(f):
#     titulo(f)
#     print('\033[30;45m', end='')
#     help(f)
#     print('\033[m', end='')
#
#
# while True:
#     titulo(tit=True)
#     pesquisa = str(input('Função ou Biblioteca > '))
#     if pesquisa in 'FIMfim':
#         titulo('fim')
#         break
#     funcao(pesquisa)
from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;0;41m',  # 1 - vermelho
     '\033[0;0;42m',  # 2 - verde
     '\033[0;0;43m',  # 3 - amarelo
     '\033[0;0;44m',  # 4 - azul
     '\033[0;0;45m',  # 5 - roxo
     '\033[7;0;40m'      # 6 - branco
     )  # A solução da tupla com cores realmente facilita o trabalho durante o código (também fica mais legível)


def ajuda(com): # Um parâmetro com o texto diminui o tamanho de código dentro da função
    titulo(f'Acessando o manual do \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0): # Diminuiu bastante o tamanho da função dentro do titulo
    tam = len(msg) + 4
    print(c[cor], end='')   # Uma tupla com acesso universal facilita na hora de colocar várias cores no programa
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEM DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)





















