# abrindo = 0
# fechando = 0
# expressao = str(input("Digite uma expressão numérica: "))
# for i in expressao:
#     if i == '(':
#         abrindo += 1
#     elif i == ')':
#         fechando += 1
# print('Expressão inválida' if abrindo > fechando or fechando > abrindo else 'Expressão válida')

expressao = str(input('Digite uma experssão: '))
pilha = []
for i in expressao:
  if i == '(':
    pilha.append('(')
  elif i == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append('(')
      break
if len(pilha) > 0:
  print('Expressão inválida')
else:
  print('Expressão válida')
      