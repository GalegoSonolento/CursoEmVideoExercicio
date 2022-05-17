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


