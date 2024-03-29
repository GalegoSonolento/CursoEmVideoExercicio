from time import sleep
from Exercícios_gerais.ex115.lib.arquivo import arqExiste, criarArquivo, lerArquivo, cadastrar
from Exercícios_gerais.ex115.lib.interface import menu, cabecalho, leiaInt

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Adicionar pessoas', 'Sair do programa'])
    if resposta == 1:
        #Opção de lista o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # cabecalho('Opção 2')
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)
