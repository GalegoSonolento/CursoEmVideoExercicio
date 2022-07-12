# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

abrindo = 0
fechando = 0
expressao = str(input("Digite uma expressão numérica: "))
for i in expressao:
    if i == '(':
        abrindo += 1
    elif i == ')':
        fechando += 1
print('Expressão inválida' if abrindo > fechando or fechando > abrindo else 'Expressão válida')
