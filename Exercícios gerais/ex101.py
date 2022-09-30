# # Exercício Python 101: Crie um programa que tenha uam função chamada voto()
# # que vai receber como parâmetro o ano de nascimento de uma pessoa,
# # retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# import datetime
#
# def voto(n):
#     print('-' * 30)
#     idade = datetime.date.today().year - n
#     print(f'Com {idade} anos: ', end='')
#     if 18 > idade > 15 or idade > 65:
#         return 'VOTO OPCIONAL'
#     elif idade < 16:
#         return 'NÃO VOTA'
#     else:
#         return 'VOTO OBRIGATÓRIO'
#
#
# # Programa principal
# print(voto(int(input('Em que ano você nasceu? '))))


def voto(ano):
    from datetime import date   # Também existe o escopo de importação de bibliotecas, da mesma forma que as variáveis
    idade = date.today().year - ano   # O escopo economiza memória tbm
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


































