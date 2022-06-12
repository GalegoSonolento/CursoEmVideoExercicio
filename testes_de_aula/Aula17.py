# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# # num.sort()
# num.sort(reverse=True)
# num.insert(2, 2)
# num.remove(2) #Procura a primeira ocorrência
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 4')
# # num.pop()
# # num.pop(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = [] #OU pode cirar vazia assim: list()
# # valores.append(5)
# # valores.append(9)
# # valores.append(4)
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor para a lista: ')))
#
# for c, v in enumerate(valores): #enumerate pega tanto a chave quanto os valores
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista')

a = [2, 3, 4, 6, 7]
b = a #Quando se iguala uma lista a outra, se cria uma ligação entre as duas
c = a[:] #Isso sim é uma cópia da lista a
b[2] = 8
c[2] = 0
print(f'Lista a: {a}')
print(f'Lista b: {b}')
print(f'Lista c: {c}')