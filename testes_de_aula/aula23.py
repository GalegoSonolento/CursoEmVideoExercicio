# É possível fazer vários blocos de tratamento de erros ao mesmo tempo (ficam na ordem de preferência de excecução
try:    # Começo do tratamento de erro
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir números por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não inserir os dados')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}') # Essa linha assim só n dá erro quando a exceção não é ativada - NameError - r só é criado quando dá certo
finally:
    print('Volte sempre! Muito Obrigado!')
