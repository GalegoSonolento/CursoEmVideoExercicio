# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

import leitor_de_inteiro

p = str(input('Digite um inteiro: '))
num = leitor_de_inteiro.leiaInt(p)
while num == -1:
    p = str(input('Digite um inteiro: '))
    num = leitor_de_inteiro.leiaInt(p)
print(f'O número é: {num}')
