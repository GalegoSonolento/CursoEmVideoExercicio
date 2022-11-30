import Desafio.des115.UI as ui


def roda_programa():
    resp = ui.apontamento_de_opcoes()
    while resp != -1:
        resp = ui.apontamento_de_opcoes()
    ui.cabecalho_do_menu('Saindo do sistema... Até logo!')