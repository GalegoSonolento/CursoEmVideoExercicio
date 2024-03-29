from time import sleep

tam_linha = 40
opcao_min = 1
opcao_max = 3


def cabecalho_do_menu(display):
    print('-' * tam_linha)
    print(f'{display:^40}')
    print('-' * tam_linha)


def opcoes_do_menu():
    sleep(0.5)
    cabecalho_do_menu('MENU PRINCIPAL')
    print('\033[33m1 - \033[34mVer pessoas cadastradas')
    print('\033[33m2 - \033[34mCadastrar nova pessoa')
    print('\033[33m3 - \033[34mSair do sistema\033[m')
    print('-' * tam_linha)


def escolha_usuario(retry=False):
    if retry:
        return input('Sua opção: ')
    opcoes_do_menu()
    return input('\033[33mSua opção: \033[m')


def testa_escolha():
    opcao = escolha_usuario()
    while True:
        try:
            opcao = int(opcao)
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            opcao = escolha_usuario(True)
        else:
            if opcao < opcao_min or opcao > opcao_max:
                print('\033[31mERRO: Digite uma opção válida!\033[m')
                opcao = escolha_usuario()
            else:
                break
    return opcao


def apontamento_de_opcoes():
    opcao = testa_escolha()
    if opcao == 1:
        cabecalho_do_menu('Opção 1')
        return 1
    elif opcao == 2:
        return 2
    elif opcao == 3:
        return -1


def printarDadosDict(dados_dict):
    for k in dados_dict:
        print(f'{k:<30} {dados_dict[k]:>3} anos')


def display_novo_user():
    new_user = dict()
    new_user['nome'] = str(input('Nome: '))
    while True:
        idade = str(input('Idade: '))
        if idade.isnumeric():
            new_user['idade'] = int(idade)
            break
        print('Idade deve ser um número inteiro')

    return new_user
