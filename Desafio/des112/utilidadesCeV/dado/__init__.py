# import moeda
from Desafio.des112.utilidadesCeV import moeda


def leiaDinheiro(num, t_aumento, t_diminuicao):
    if num < 0 or t_diminuicao < 0 or t_aumento < 0:
        return 'Valor não monetário'
    moeda.resumo(num, t_aumento, t_diminuicao)
    return ' '


def leiaDinheiro2(num):
    while not num.isnumeric():
        print(3)
        # Aqui vou mostrar a mensagem de erro e pedir o input novamente
    if num.isnumeric():
        return 'Deu certo'
    return f'ERRO: "{num}" é um preço inválido'
