nome = str(input('Quyal seu nome? '))
if nome == 'Gustavo':
    print('Belo nome')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome femonino')
print('Tenha um bom dia, {}'.format(nome))