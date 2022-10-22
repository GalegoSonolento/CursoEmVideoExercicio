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
