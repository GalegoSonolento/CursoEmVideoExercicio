# # Melhore o desafio 61, perguntando para o usuário se elçe quer mostrar mais alguns termos. O program encerra
# # quando ele disser que quer mostrar 0 termos
# a1 = int(input('Digite o primeiro temo da PA: '))
# r = int(input('Digite a razão dessa PA: '))
# termos = 10
# cont = 1
# while cont <= termos:
#     print('{}° termo: {}'.format(cont, a1 + (cont - 1) * r))
#     cont += 1
# maisTermos = True
# while maisTermos:
#     mais = int(input('Digite quantos mais termos você deseja visualizar (digite zero para finalizar o programa): '))
#     if mais <= 0:
#         print('Não se mostra mais zero ou de trás para frente!')
#         maisTermos = False
#     else:
#         for i in range(0, mais):
#             print('{}° termo: {}'.format(cont, a1 + (cont - 1) * r))
#             cont += 1

print('Gerador de PA')
print('-=='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
