# limite = 1
# quebra = False
# i = 0
# total = 0
# prodMaisMil = 0
# maisBarato = ''
# precoBarato = 0
# j = 0
# print('='*30)
# print('MERCADINHO BIG BON')
# print('='*30)
# print('Veja as promoções e escolha seus produtos à vontade!')
# print('_'*30)
# while True:
#     prod = str(input('Digite o nome do produto que deseja adquirir: '))
#     while True:
#         preco = float(input('Digite o preço deste produto: '))
#         if preco <= 0:
#             print('O produto não pode ser de graça.')
#         else:
#             break
#     total += preco
#     if preco > 1000:
#         prodMaisMil += 1
#     if j == 0:
#         precoBarato = preco
#         maisBarato = prod
#         j += 1
#     else:
#         if precoBarato > preco:
#             precoBarato = preco
#             maisBarato = prod
#     while i < limite:
#         opcao = str(input('Deseja continuar as compras [S/N]? ')).strip().upper()[0]
#         if opcao == 'N':
#             quebra = True
#         elif opcao not in 'SN':
#             print('Opção inválida. Digite novamente.')
#             limite += 1
#         i += 1
#     i = 0
#     if quebra:
#         break
# print(f'Você gastou {total} reais')
# print(f'{prodMaisMil} produtos custaram mais que mil reais')
# print(f'O produto mais barato é {maisBarato}')
# print('Volte sempre!')

soma = totMil = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    soma += preco
    if preco > 1000:
        totMil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {soma:.2f}')
print(f'{totMil} produtos foram mais de 1000 reais')
print(f'O produto mais barato é {barato}')
