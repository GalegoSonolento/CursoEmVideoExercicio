# cont = cA = cE = cI = cO = cU = 0
# tupla = ('maçã', 'pera', 'banana', 'caderno', 'lapizeira', 'compilador', 'Otorrinolaringologista')
# for i in range(0, len(tupla)):
#     listaTermo = list(tupla[i])
#     for j in range(0, len(listaTermo)):
#         if listaTermo[j] in 'aAeEiIoOuU' and cont == 0:
#             print(f'O termo {tupla[i]} tem as seguintes vogais: ')
#             cont += 1
#         if listaTermo[j] in 'aA' and cA == 0:
#             print('A')
#             cA += 1
#         elif listaTermo[j] in 'eE' and cE == 0:
#             print('E')
#             cE += 1
#         elif listaTermo[j] in 'iI' and cI == 0:
#             print('I')
#             cI += 1
#         elif listaTermo[j] in 'oO' and cO == 0:
#             print('O')
#             cO += 1
#         elif listaTermo[j] in 'uU' and cU == 0:
#             print('U')
#             cU += 1
#     cont = cA = cE = cI = cO = cU = 0

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador',
            'futuro')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end=' ')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, end=' ')
