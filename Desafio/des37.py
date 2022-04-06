# Escreva um rpograma que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
#1 - binário
#2 - octal
#3 - hexadecimal
num = int(input('Digite um número para a máquina: '))
print('Qual conversão deseja fazer? '
      '\n [1] converter para BINÁRIO'
      '\n converter para OCTAL'
      '\n converter para HEXADECIMAL')
escolha =
binary = format(int(input('Digite um valor inteiro: ')), 'b')
print(binary)
octal = "{0:o}".format(int(input('Digite outro valor inteiro: ')))
print(octal)
print(format(int(input("Digite um número float: ")), 'x'))
