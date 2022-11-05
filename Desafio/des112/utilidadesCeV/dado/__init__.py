# import moeda
from Desafio.des112.utilidadesCeV import moeda


def leiaDinheiro(msg): # Pra deixar melhor que isso é preciso ter tratamento de erros com python
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


# def leiaDinheiro(num, t_aumento, t_diminuicao):
#     if num < 0 or t_diminuicao < 0 or t_aumento < 0:
#         return 'Valor não monetário'
#     moeda.resumo(num, t_aumento, t_diminuicao)
#     return ' '
#
#
# def leiaDinheiro2(entrada):
#     teste = entrada
#     entrada.replace(',', '')
#     while not teste.isnumeric():
#         print(f'ERRO: "{teste}" é um preço inválido')
#         entrada = str(input('Digite o preço: R$')).replace(',', '')
#         teste = entrada
#     num = float(entrada)
#     print(num)
#     if num == 2:
#         return 'Deu certo'
