# def fatorial(ent, show=False):
#   """
#   fatorial(ent, show=False)
#   param n: número a ser calculado
#   param show: (opcional) Mostrar ou não o cálculo
#   return: O valor do fatorial de um número n
#   """
#   print('-' * 30)
#   respShow = ''
#   num = ent
#   for i in range(num - 1, 0, -1):
#     if show and i == num - 1:
#       respShow += f'{num} * {i} '
#     elif show:
#       respShow += f'* {i} '
#       if i == 1:
#         respShow += '= '
#     num *= i
#   return respShow + f'{num}'

  
# # Programa principal
# print(fatorial(5, True))
# help(fatorial)


def fatorial(n, show=False):
  """
  -> Calcula o fatorial de um número:
  param n: número para cálculo
  param show: mostra ou não o cálculo (opcional)
  return: resultado do fatorial
  """
  f = 1
  for i in range(n, 0, -1):
    if show:  # Simplesmente uma iterção de prints
      print(i, end=' ')
      if i > 1:
        print(' x', end=' ')
      else:
        print('= ', end='')
    f *= i
  return f


# Programa principal
print(fatorial(5, show=False))
help(fatorial)
