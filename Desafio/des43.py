# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
#tabela abaixo:
#- abaixo de 18.5: abaixo do peso
#- Entre 18.5 e 25:peso ideal
#- 25 até 30: sobrepeso
#- 30 até 40: obesidade
#- Acima de 40: obesidade mórbida
import math
print('Seu Índice de Massa Corporal será calculado de acordo com os seguintes parâmetros:'
      '\n - abaixo de 18.5: abaixo do peso'
      '\n - Entre 18.5 e 25:peso ideal'
      '\n - 25 até 30: sobrepeso'
      '\n - 30 até 40: obesidade'
      '\n - Acima de 40: obesidade mórbida')
peso = float(input('Digite aqui seu peso: '))
altura = float(input('Digite aqui sua altura em metros: '))
imc = peso / (math.pow(altura, 2))
