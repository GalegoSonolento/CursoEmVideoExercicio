# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de
# pagamento
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros
preco = 100
print('Você deliberadamente vai comprar um tatu assado por 100 mangos '
      '\n Por favor digite a forma de pagamento abaixo:'
      '\n 1 - À vista em dinheiro/ cheque (10% de desconto)'
      '\n 2 - À vista no cartão (5% de desconto)'
      '\n 3 - Em até 2x no cartão (preço normal)'
      '\n 4 - 3x ou mais no cartão (20% de juros)')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
      precoN = preco - (preco * 0.1)
      print('Pagarás {}'.format(precoN))
elif opcao == 2:
      precoN = preco - (preco * 0.05)
      print('pagrás R${}'.format(precoN))
elif opcao == 3:
      print('Pagarás R${}'.format(preco))
elif opcao == 4:
      precoN = preco + (preco * 0.2)
      print('Pagarás R${}'.format(precoN))
