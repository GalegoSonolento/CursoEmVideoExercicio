somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for i in range(1, 5):
    print('---- {}° Pessoa ----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M;F]: ').strip())
    somaIdade += idade
    if i == 1 and sexo in 'Mn':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mn' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O nome do homem mais velho é {}, de {} anos'.format(nomeVelho, maiorIdadeHomem))
print('Existem {} mulheres menores de 20 anos nesse grupo'.format(totmulher20))
