# import uteis    # Conceito básico de modularização própria
# from uteis import triplo, fatorial  # Forma não muito recomendada - funções podem ser conflitantes
# Se outra importação também tiver a função dobro acontece um problema (em geral o python usa a última importada)
from uteis import numeros

# Programa Principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é5 {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
