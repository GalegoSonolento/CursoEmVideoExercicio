#Faça um program que leia um número qualquer e mostre seu fatorial
# 5! = 5.4.3.2.1 = 120
# Fazer com while e outro com for

# fator = int(input('Digite um número para realizar o fatorial: '))
# cont = fator - 1
# fatorial = fator
# while cont != 1:
#     if cont == fator - 1:
#         fatorial = fator * cont
#         cont -= 1
#     else:
#         fatorial = fatorial * cont
#         cont -= 1
# print('O fatorial de {} é {}'.format(fator, fatorial))

fator = int(input('Digite um número para realizar o fatorial: '))
fatorial = fator
for i in range(1, fator):
    fatorial = fatorial * i
print('Fatorial de {} é {}'.format(fator, fatorial))
