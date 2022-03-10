# Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada

num = int(input('Digite um número inteiro qualquer: '))

print('A tabuada é: \n 1x{1}={2} \n 2x{1}={3} \n 3x{1}={4} \n 4x{1}={5} \n 5x{1}={6}'
      '\n 6x{1}={7} \n 7x{1}={8} \n 8x{1}={9} \n 9x{1}={10}'.format(num, num, num, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9))