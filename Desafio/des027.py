# FAça um prograam que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# EX: Ana Maria de Souza
# primeiro = Ana
# último = Souza
nome = str(input('Digite seu nome completo: ')).lower().strip()
primeiro = nome.split()
print(primeiro[0].capitalize())
count = -1
for i in primeiro:
    count += 1
print(primeiro[count].capitalize())
