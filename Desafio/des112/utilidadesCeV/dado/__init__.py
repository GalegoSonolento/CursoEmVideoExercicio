# import moeda
from Desafio.des112.utilidadesCeV import moeda


def leiaDinheiro(num, t_aumento, t_diminuicao):
    if num < 0 or t_diminuicao < 0 or t_aumento < 0:
        return 'Valor não monetário'
    moeda.resumo(num, t_aumento, t_diminuicao)
    return ' '


def leiaDinheiro2(entrada):
    while not entrada.isnumeric():
        print(f'ERRO: "{entrada}" é um preço inválido')
        entrada = entrada(input('Digite o preço: R$'))
    num = float(entrada)
    print(num)
    if num == 2:
        return 'Deu certo'
