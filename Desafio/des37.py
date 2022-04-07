# Escreva um rpograma que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
#1 - binário
#2 - octal
#3 - hexadecimal
num = int(input('Digite um número para a máquina: '))
print('Qual conversão deseja fazer? '
      '\n [1] converter para BINÁRIO'
      '\n [2] converter para OCTAL'
      '\n [3] converter para HEXADECIMAL')
escolha = int(input('Digite sua escolha aqui: '))
if escolha == 1:
      binary = format(num, 'b')
      print(binary)
elif escolha == 2:
      octal = "{0:o}".format(num)
      print(octal)
elif escolha == 3:
      print(format(num, 'x'))
