def aumentar(n, taxa, format=False):
    res = n + (n * taxa / 100)
    if format:
        return moeda(res)
    return res


def diminuir(n, taxa, format=False):
    res = n - (n * taxa / 100)
    if format:
        return moeda(res)
    return res


def dobro(n, format=False):
    res = n * 2
    if format:
        return moeda(res)
    return res


def metade(n, format=False):
    res = n / 2
    if format:
        return moeda(res)
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(valor=0, t_aumento=10, t_diminuicao=5):
    '''
    Printa um resumo para o usuário dos dados mínimos do valor
    :param valor: número para cálculo
    :param t_aumento: taxa de aumento
    :param t_diminuicao: taxa de redução
    :return: inexistente
    '''
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor):^13}')
    print(f'Dobro do preço: \t{dobro(valor, True):^13}')
    print(f'Metade do preço: \t{metade(valor, True):^13}')
    print(f'{t_aumento}% de aumento: \t{aumentar(valor, t_aumento, True):^13}')
    print(f'{t_diminuicao}% de redução: \t{diminuir(valor, t_diminuicao, True):^13}')
    print('-'*30)
