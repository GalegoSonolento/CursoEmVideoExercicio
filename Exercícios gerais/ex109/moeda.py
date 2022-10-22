def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return moeda(res)


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return moeda(res)


def dobro(preco):
    res = preco * 2
    return moeda(res)


def metade(preco):
    res = preco / 2
    return moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

