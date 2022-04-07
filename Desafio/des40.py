# Crie um programa que lea duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#- Média abaixo de 5.0 - reprovado
#- média entre 5.0 e 6.9 - recuperação
#- média 7.0 ou superior - aprovado
print('Você colocará suas notas e o cálculo será baseado nos seguintes cirtérios:'
      '\n - Média abaixo de 5.0 - reprovado'
      '\n - Média entre 5.0 e 6.9 - recuperação'
      '\n - Média 7.0 ou superior - aprovado')
n1 = float(input('Digite sua nota na primeira avaliação: '))
n2 = float(input('Digite sua nota na segunda avaliação: '))
media = (n1 + n2)/2
if media < 5.0:
    print('Sua média foi abaixo de 5 pontos'
          '\n \033[1;31m REPROVADO \033[m')
elif 5.0 <= media <= 6.9:
    print('Sua média permaneceu entre 5 e 6.9 pontos '
          '\n \033[1;33m RECUPERAÇÃO \033[m')
elif media >= 7.0:
    print('Sua média foi maior que 7 pontos'
          '\n \033[1;34m APROVADO \033[m')
