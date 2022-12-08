# # Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# # vai retornar um dicionário com as seguintes informações:
# #
# # – Quantidade de notas
# # – A maior nota
# # – A menor nota
# # – A média da turma
# # – A situação (opcional)
#
#
# def notas(*n, sit=False):
#     """
#     -> Função para calcular a maior, menor e nota média do aluno,
#     bem como sua situação.
#     :param n: uma ou mais notas que calculam a média do aluno
#     :param sit: parâmetro que ativa ou não a vizualização da situação do aluno
#     :return: dicionário com várias informações das notas do aluno
#     """
#     menor_nota = maior_nota = soma = 0
#     for i, j in enumerate(n):
#         if i == 0:
#             menor_nota = maior_nota = j
#         if menor_nota > j:
#             menor_nota = j
#         if maior_nota < j:
#             maior_nota = j
#         soma += j
#     media = soma / len(n)
#     dic = {'total: ': len(n), 'maior: ': maior_nota, 'menor: ': menor_nota, 'média: ': media}
#     situacao = 'RUIM'
#     if sit:
#         if media >= 7:
#             situacao = 'BOA'
#         elif 5 <= media < 7:
#             situacao = 'RAZOÁVEL'
#         dic['situacao'] = situacao
#     return dic
#
#
# #Programa principal
# resp = notas(2, 9, 4, 10, 10, sit=True)
# print(resp)
# help(notas)


def notas(*n, sit=False):
    """
    -> Função para analisar várias notas de alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: mostra a situação dos alunos
    :return: dicionário que mostra diversas informações do aluno.
    """
    r = dict()  # Aparentemente todos esses métodos substituem os for e ifs gigantescos que eu escrevia no código
    r['total'] = len(n) # Existem várias funções parecidas com o len()
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 8.5, 10, 4.5, 6.7, sit=True) # A variável 'sit' precisa ser indicada para funcionar o True
print(resp)
help(notas)




















