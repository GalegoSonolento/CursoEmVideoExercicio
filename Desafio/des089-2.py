# Exercício Python 089: crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo numa lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

listaComp = list()
while True:
    nome = str(input("Digite o nome: "))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    listaComp.append([nome, [nota1, nota2]])
    print(listaComp)
    resposta = str(input('Deseja continuar? [S/N]')).strip()[0]
    if resposta in 'nN':
        break
print('-=' * 30)
print(f'{"No.":<4}', f'{"NOME":<10}', f'{"MÉDIA":>8}')
print('-' * 30)
for i, j in enumerate(listaComp):
    print(f'{i:<4}', f'{j[0]:<10}', f'{(j[1][0] + j[1][1]) / 2:>8}')
print('-' * 30)
resp = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
while resp != 999:
    print(f'Notas de {listaComp[resp][0]}: {listaComp[resp][1]}')
    resp = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
print('-=' * 30)
print('<VOLTE SEMPRE>')
