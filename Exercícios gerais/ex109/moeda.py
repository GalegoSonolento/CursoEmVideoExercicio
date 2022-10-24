# def aumentar(preco=0, taxa=0):
#     res = preco + (preco * taxa / 100)
#     return moeda(res)
#
#
# def diminuir(preco=0, taxa=0):
#     res = preco - (preco * taxa / 100)
#     return moeda(res)
#
#
# def dobro(preco):
#     res = preco * 2
#     return moeda(res)
#
#
# def metade(preco):
#     res = preco / 2
#     return moeda(res)
#
#
# def moeda(preco=0, moeda='R$'):
#     return f'{moeda}{preco:.2f}'.replace('.', ',')
#

def aumentar(n, taxa, format=False):
    '''
    Aumenta x porcento
    :param n: valor a ser calculado
    :param taxa: porcentagem de aumento
    :param format: se será formatado ou não
    :return: cálculo, formatado ou não
    '''
    res = n + (n * taxa / 100)
    return res if format is False else moeda(res) # Condição de formatação - o atributo precisa ser falso para que o código não quebre
    # O python tem uma linguagem mais escrita


def diminuir(n, taxa, format=False):
    '''
    Diminui x porcento
    :param n: Valor que recebe o cálculo
    :param taxa: taxa de diminuição
    :param format: com ou sem formatação
    :return: cálculo com ou sem formatação
    '''
    res = n - (n * taxa / 100)
    return res if format is False else moeda(res)


def dobro(n, format=False):
    '''
    Dobra do valor do número
    :param n: valor para cálculo
    :param format: com ou sem formatação
    :return: cálculo com ou sem formatação
    '''
    res = n * 2
    return res if format is False else moeda(res)


def metade(n, format=False):
    '''
    Divide um número pela metade
    :param n: valor para cálculo
    :param format: com ou sem formatação
    :return: cálculo com ou sem formatação
    '''
    res = n / 2
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    '''
    Detém a formatação das respostas
    :param preco: valor para formatação
    :param moeda: qual unidade monetária será formatado
    :return: valor formatado
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')
