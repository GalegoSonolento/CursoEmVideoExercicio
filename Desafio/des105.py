# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*n, sit=False):
    menor_nota = maior_nota = soma = 0
    for i, j in enumerate(n):
        if i == 0:
            menor_nota = maior_nota = j
        if menor_nota > j:
            menor_nota = j
        if maior_nota < j:
            maior_nota = j
        soma += j
    media = soma / len(n)
    dic = {'total: ': len(n), 'maior: ': maior_nota, 'menor: ': menor_nota, 'média: ': media}
    situacao = 'RUIM'
    if sit:
        if media >= 7:
            situacao = 'BOA'
        elif 5 <= media < 7:
            situacao = 'RAZOÁVEL'
        dic['situacao'] = situacao
    return dic


#Programa principal
resp = notas(2, 3, 10, sit=True)
print(resp)
