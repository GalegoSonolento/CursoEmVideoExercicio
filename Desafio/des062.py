# Melhore o desafio 61, perguntando para o usuário se elçe quer mostrar mais alguns termos. O program encerra
# quando ele disser que quer mostrar 0 termos
a1 = int(input('Digite o primeiro temo da PA: '))
r = int(input('Digite a razão dessa PA: '))
termos = 10
cont = 1
while cont <= termos:
    print('{}° termo: {}'.format(cont, a1 + (cont - 1) * r))
    cont += 1
maisTermos = True
while maisTermos:
    mais = int(input('Digite quantos mais termos você deseja visualizar (digite zero para finalizar o programa): '))
    if mais <= 0:
        print('Não se mostra mais zero ou de trás para frente!')
        maisTermos = False
    else:
        for i in range(0, mais):
            print('{}° termo: {}'.format(cont, a1 + (cont - 1) * r))
            cont += 1
