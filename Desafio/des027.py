# FAça um prograam que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# EX: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str(input('\033[31m Digite seu nome completo: ')).lower().strip()
primeiro = nome.split()
print('\033[32m ', primeiro[0].capitalize())
count = -1
for i in primeiro:
    count += 1
print('\033[33m ', primeiro[count].capitalize())
