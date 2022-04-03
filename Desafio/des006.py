# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e
# raíz quadrada

num = float(input('\033[35m Digite um número qualquer: '))

print('\033[37m Você digitou {}, seu dobro é {}, \n seu triplo é {} e sua raiz quadrada é {}.'.format(num, num*2, num*3,
                                                                                             num**(1/2)))