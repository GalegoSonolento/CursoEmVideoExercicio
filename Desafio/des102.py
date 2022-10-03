# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(ent, show=False):
   """
  fatorial(ent, show=False)
  param n: número a ser calculado
  param show: (opcional) Mostrar ou não o cálculo
  return: O valor do fatorial de um número n
  """
  print('-' * 30)
  respShow = ''
  num = ent
  for i in range(num - 1, 0, -1):
    if show and i == num - 1:
      respShow += f'{num} * {i} '
    elif show:
      respShow += f'* {i} '
      if i == 1:
        respShow += '= '
    num *= i
  return respShow + f'{num}'

  
# Programa principal
print(fatorial(5, show=True))
help(fatorial)
