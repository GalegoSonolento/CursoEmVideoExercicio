# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
# preciso fazer uma classe de acesso que vai identificar se já existe um arquivo, vai lê-lo e escrever nele
# Dentro da util talvez?

arquivo = open('./resources/files/teste2.txt', 'w')
arquivo.write('Cai de cabeça')
arquivo.write('Kinda sus')
arquivo.close()

