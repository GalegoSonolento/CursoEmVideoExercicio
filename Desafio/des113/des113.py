# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

import leitor_de_numero

p = str(input('Digite um inteiro: '))
num = leitor_de_numero.leiaInt(p)
while num == -1:
    p = str(input('Digite um inteiro: '))
    num = leitor_de_numero.leiaInt(p)
p2 = str(input('Digite um número real: '))
numr = leitor_de_numero.leiaReal(p2)
while numr == -1:
    p2 = str(input('Digite um número real: '))
    numr = leitor_de_numero.leiaReal(p2)
print(f'O número inteiro é: {num}')
print(f'O número real é: {numr}')
