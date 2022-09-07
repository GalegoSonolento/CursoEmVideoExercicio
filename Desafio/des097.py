# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva (‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(escr):
    a = len(escr)+4
    b = escr
    print('~'*a)
    print(f'  {escr}')
    print('~'*a)


escreva('SUA MÃE É MINHA')
escreva('LOS RAPAZES')
escreva('STONKS')
