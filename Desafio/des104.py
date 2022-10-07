# Exercício Python 104: Crie um programa que só tenha a função leiaInt(),
# que vai funcionar de forma semelhante à função input do Python, só que fazendo a validação para aceitar apenas
# um valor numérico. Ex: leiaInt('Digite um n:')

def leiaInt(txt):
    new_input = str(input(txt))
    while not new_input.isnumeric():
        print('\033[31m ERRO! Digite apenas um número!\033[37m')
        new_input = str(input(txt))
    return new_input


# Programa principal
n = leiaInt("Dígite um numeral: ")
print(f'Você acabou de digitar {n}')