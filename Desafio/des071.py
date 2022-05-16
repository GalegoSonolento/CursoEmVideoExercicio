# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada serão entregues
#OBS: Considere que o caixa posusi cédulas de R$50, R$20, R$10 e R$1

nota50 = nota20 = nota10 = nota1 = saque = 0
while True:
    valor = int(input("Digite o valor a ser sacado [apenas números inteiros]: "))
    saque = valor
    if valor <= 0:
        print("Você não pode sacar valores negativos!")
    else:
        break
while True:
    if valor >= 50:
        valor -= 50
        nota50 += 1
    elif valor >= 20:
        valor -= 20
        nota20 += 1
    elif valor >= 10:
        valor -= 10
        nota10 += 1
    elif valor >= 1:
        valor -= 1
        nota1 += 1
    else:
        break
print(f"Seu saque de {saque} reais virá com {nota50} notas de 50, {nota20} notas de 20, {nota10} notas de 10 e {nota1} "
      f"notas de 1")
