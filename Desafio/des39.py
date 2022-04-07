# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar
#- Se é a hora de se alista
#- Se já passou do tempo do alistamento
# Seu programa também deverpa mostrar o tempo que falta ou que passou do prazo
idade = int(input('Jovem, qual a sua idade? '))
if idade < 18:
    temp = 18 - idade
    print('Jovem, em {} anos você precisará realizar o alistamento militar!'.format(temp))
elif idade == 18:
    print('Jovem, você tem até o próximo junho para concluir seu alistamento militar!')
elif idade > 18:
    temp = idade - 18
    print('Jovem, você deveria ter feito o alistamento {} anos atrás'
          '\n Entre em contato imediataemnte com a junta militar da sua cidade e relize o processo de alistamento'
          '\n o quanto antes.'.format(temp))
