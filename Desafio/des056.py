# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos
listaNome = []
listaIdade = []
listaSexo = []

manoVelho = 0
nomeMenoVelho = 'Não existem homens no grupo'
minaMenos20 = 0
for i in range(1, 5):
    print('---- {}° PESSOA ----'.format(i))
    nome = str(input('Digite o nome: '))
    listaNome.append(nome)
    idade = int(input('Digite a idade: '))
    listaIdade.append(idade)
    sexo = str(input('Digite o sexo(M/F): ')).upper()
    listaSexo.append(sexo)
    if i == 1 and sexo == 'M':
        manoVelho = idade
        nomeMenoVelho = nome
    elif sexo == 'M':
        if idade > manoVelho:
            manoVelho = idade
            nomeMenoVelho = nome
    if sexo == 'F':
        if idade < 20:
            minaMenos20 += 1

somaIdade = 0
media = 0
cont = 0
for j in listaIdade:
    somaIdade += j
    cont += 1
media = somaIdade / cont
print('A media de idade do grupo é {}'.format(media))

if manoVelho == 0:
    print(nomeMenoVelho)
else:
    print('O nome do homem mais velho é {}'.format(nomeMenoVelho))

print('Exitem {} mulheres menores de 20 anos nesso grupo'.format(minaMenos20))
