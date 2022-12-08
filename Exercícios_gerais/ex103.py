# # Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# # o nome de um jogador e quantos gols ele marcou.
# # O programa deverá ser capaz de mostrar a ficha do jogador,
# # mesmo que algum dado não tenha sido informado corretamente.
#
# def ficha(nome, gols):
#     nomeJog = nome.replace(" ", "")
#     numGols = 0
#     nomePlayer = '<desconhecido>'
#     if gols.isnumeric():
#         numGols = gols
#     else:
#         numGols = 0
#     if nome.isalpha():
#         nomePlayer = nome
#     print(f'O jogador {nome}, fez {numGols} gol(s) no campeonato.')
#
#
# # Programa principal
# nome = str(input("Nome do jogador: ")).strip()
# gols = str(input("Número de gols: "))
# ficha(nome, gols)


def ficha(jog='<desconhecido>', gol=0): # Apesar de poder ser feito tudo dentro do método, o Guanabara testou todos os
    # valores antes de chamar o método (que foi apenas um print)
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():   # lá atrás teve a instrução de tratamento de strings e esse era um dos comandos comuns
    g = int(g)
else:
    g = 0
if n.strip() == '': # Esse método de verificação ficou mais elegante que o meu (poupa linhas de código)
    ficha(gol=g) # Dois tipos de chamamento diferentes são possíveis (não precisa de valores padrões nos parâmetros do método)
else:
    ficha(n, g)




















