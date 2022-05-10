# Crie um programa que leia vário número s inteiros pelo teclado. O prograama só vai para quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostra quantos número sforam digitados e qual fio a soma entre eles
#(desconsiderando o flag)

cont = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro [ou 999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'Foram digitados {cont} números, com soma de {soma}.')
