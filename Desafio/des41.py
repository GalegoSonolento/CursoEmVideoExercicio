# A confederaçãoo nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
#- até 9 - mirim
#- até 14 - infantil
#- até 19 - junior
#- até 20 - sênior
#- acima - master
print('Digite sua idade e mostraremos sua categoria na natação seguindo os critérios:'
      '\n - até 9 - mirim'
      '\n - até 14 - infantil'
      '\n - até 19 - junior'
      '\n - até 20 - sênior'
      '\n - acima - master')
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Você é um nadador mirim')
elif 9 < idade <= 14:
    print('Você é um nadador infantil')
elif 14 < idade <= 19:
    print('Você é um nadador júnior')
elif 19 < idade <= 20:
    print('Você é um nadador sênior')
elif idade > 20:
    print('Você um MASTER nadador')
