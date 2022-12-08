# # Crie um programa que leia vários número inteiros pelo teclado. O programa só vai para quando o usuário digitar o
# # valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# # entre eles (desconsiderando o flag)
#
# num = int(input('Digite um número para o sistema [999 para parar]: '))
# soma = num
# while num != 999:
#     num = int(input('Digite outro número para o sistema [999 para parar]: '))
#     if num != 999:
#         soma += num
# print('A soma de todos os números digitados é {}'.format(soma))

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
