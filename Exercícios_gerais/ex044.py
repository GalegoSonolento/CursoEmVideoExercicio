print('{:=^40}'.format(' LOJAS TEU PAI '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cjeque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual a opção? "))
if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('\033[31m OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')
print('Sua compra de R&{:.2f} vai custar R${:.2f} no final'.format(preco, total))
