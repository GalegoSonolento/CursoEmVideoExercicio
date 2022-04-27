from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    idade = atual - nasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('Ao todo tivemos {} pessoa menores de idade'.format(menores))