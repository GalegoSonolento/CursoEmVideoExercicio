import Desafio.des115.UI as ui
import Desafio.des115.resources as files


def roda_programa():
    files.jsonFiles(1, False)
    resp = ui.apontamento_de_opcoes()
    while resp != -1:
        if resp == 1:
            files.jsonFiles()
        elif resp == 2:
            files.jsonFiles(2, False)
        resp = ui.apontamento_de_opcoes()
    ui.cabecalho_do_menu('Saindo do sistema... Até logo!')


def insere_pessoa():
    ui.cabecalho_do_menu("NOVO CADASTRO")
    new_cadastro = ui.display_novo_user()
