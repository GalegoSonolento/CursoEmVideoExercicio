# Exercício Python 106: Faça um mini-sistema que usa o interactive help do python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores


def titulo(tf='sas', tit=False):
    if tit:
        print('\033[42m', '~' * 30, '\n  SISTEMA DE AJUDA PyHELP', '\n', '~' * 30)
        print('\033[m', end='')
    elif tf == 'fim':
        print('\033[41m', '~' * 12, '\n', ' Até Logo! ', '\n', '~' * 12)
        print('\033[m')
    else:
        tamLinha = 28 + len(tf) + 4
        print('\033[30;44m', '~' * tamLinha, '\n', f' Acessando manual do comando "{tf}"', '\n', '~' * tamLinha)
        print('\033[m', end='')


def funcao(f):
    titulo(f)
    print('\033[30;45m', end='')
    help(f)
    print('\033[m', end='')


while True:
    titulo(tit=True)
    pesquisa = str(input('Função ou Biblioteca > '))
    if pesquisa in 'FIMfim':
        titulo('fim')
        break
    funcao(pesquisa)
