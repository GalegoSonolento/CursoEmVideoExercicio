# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos
# b) Quants homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos
# É necessário garantir que o programa funcionará para qualquer resposta

from time import sleep
quantM18 = manos = minasUnder20 = 0
while True:
    while True:
        idade = int(input('Digite a idade da pessoa: '))
        if idade > 0:
            break
    while True:
        sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
        if sexo in 'FM':
            break
    if idade < 18:
        quantM18 += 1
    if sexo == 'M':
        manos += 1
    if sexo == 'F' and idade < 20:
        minasUnder20 += 1
    opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        print('Continuando...')
        sleep(1)
print(f'Foram cadastrados {quantM18} menores de 18 anos, {manos} homens e {minasUnder20}')
