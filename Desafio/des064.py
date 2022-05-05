# Crie um programa que leia vários número inteiros pelo teclado. O programa só vai para quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag)

num = int(input('Digite um número para o sistema [999 para parar]: '))
soma = num
while num != 999:
    num = int(input('Digite outro número para o sistema [999 para parar]: '))
    if num != 999:
        soma += num
print('A soma de todos os números digitados é {}'.format(soma))
