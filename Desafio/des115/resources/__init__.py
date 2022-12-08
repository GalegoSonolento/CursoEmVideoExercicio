# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
# preciso fazer uma classe de acesso que vai identificar se já existe um arquivo, vai lê-lo e escrever nele
# Dentro da util talvez?

# arquivo = open('./resources/files/teste2.txt', 'w')
# arquivo.write('Cai de cabeça')
# arquivo.write('Kinda sus')
# arquivo.close()

# import json
#
# dict ={
#     "User1":{
#         "name": "Kinda Sus",
#         "rollno": 56,
#         "hight": 1.56,
#         "phoneNumber": "3423543454"
#     },
#     "User2": {
#         "name": "amongus",
#         "weight": 87,
#         "hight": 1.78,
#         "phoneNumber": "234234234234"
#     }
# }
# json_object = json.dumps(dict, indent=4)
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
#
# with open("sample.json", "r") as outfile:
#     json_object = json.load(outfile)
#
# print(json_object)
# print(type(json_object))


import json
from Desafio.des115.UI import *

def jsonFiles(read_write=1, printar=True):
    if read_write == 1:
        try:
            dados_dict = lerJson()
        except:
            dados_dict = {}
            criarJson(dados_dict)
        else:
            if printar:
                printarDadosDict(dados_dict)

def criarJson(dados_dict):
    json_object = json.dumps(dados_dict, indent=4)
    with open("./resources/dados.json", "w") as outfile:
        outfile.write(json_object)
    print('Arquivo de dados criado!')
    outfile.close()


def lerJson():
    with open("./resources/dados.json", "r") as file_in:
        dados_dict = json.load(file_in)
    file_in.close()
    return dados_dict
