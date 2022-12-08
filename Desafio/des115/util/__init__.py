import Desafio.des115.UI as ui
import Desafio.des115.resources as files


def roda_programa():
    files.jsonFiles(1, False)
    resp = ui.apontamento_de_opcoes()
    while resp != -1:
        if resp == 1:
            files.jsonFiles()
        resp = ui.apontamento_de_opcoes()
    ui.cabecalho_do_menu('Saindo do sistema... Até logo!')