from datetime import date
atual = date.today().year
sexo = str(input('Seu sexo é masculino(M) ou feminino(F)? ')).upper()
if sexo == 'M':
    nasc = int(input('Ano de ascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Aliste-se IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 -idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Você deveria ter se alistado em {}'.format(ano))
else:
    print('Mulheres não têm alistamento militar obrigatório')