# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
    nomeJog = nome.replace(" ", "")
    numGols = 0
    nomePlayer = '<desconhecido>'
    if gols.isnumeric():
        numGols = gols
    else:
        numGols = 0
    if nomeJog.isalpha():
        nomePlayer = nome
    print(f'O jogador {nomePlayer}, fez {numGols} gol(s) no campeonato.')


# Programa principal
nome = str(input("Nome do jogador: ")).strip()
gols = str(input("Número de gols: "))
ficha(nome, gols)
