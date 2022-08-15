# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade' : 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())      # O programa monta uma lista de tuplas para cada ítem do dicionário
# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['peso'] = 98.5      # Dicionário não faz append
# for k, v in pessoas.items():    # Dicionário não tem enumerate, ele é substituíudo pelo .items()
#     print(f'{k} = {v}')

# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil = []
# brasil.append(estado1)
# brasil.append(estado2)
# # print(brasil)       # Lista de dicionários
# # print(brasil[0])
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):       # É necessário tomar cuidado quando se passa um dicionário é preciso fazer cópia sem fatiamento
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())    # Maneira de copiar um dicionário para colocá-lo em uma lista
for e in brasil:
    for v in e.values():
        print(v, end='')
    print( )

