lanche = ('Hambúerguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
# print(lanche)
# Dps do python 3.5 não precisa mais usar parênteses
# print(lanche[-4])
# print(lanche[1:3])
# print(lanche[2:])
# print(lanche[:2])
# print(lanche[-3:])
# lanche[1] = 'Refrigerante'
# print(lanche[1])
# for c in lanche:
#     print(f'Comerei {c}')
print(len(lanche))
for c in range(len(lanche)):
    print(f'Comi {lanche[c]}')