# def soma(a, b):
#     print(f'A={a} e B={b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#
#
# # Prgrama principal
# # a = 4
# # b = 5
# # s = a + b
# # print(s)
# # # OU
# # soma(4, 5)
# #
# # a = 8
# # b = 9
# # s = a + b
# # print(s)
# # # OU
# # soma(8, 9)
# #
# # a = 2
# # b = 1
# # s = a + b
# # print(a + b)
# # # OU
# # soma(2, 1)
#
# soma(b=4, a=5)  # Python permite a troca de ordem dos parâmtros - se não explicitar ele vai no padrão montado


# def contador(* num):
#     # print(num)      # Ele cria uma tupla automaticamente pra armazenamento
#     # for v in num:
#     #     print(v, end=' ')
#     # print()
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')
#
#
# contador(2, 1, 4)
# contador(8, 0)
# contador(5, 7, 78, 9)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 4, 6, 12, 90]
dobra(valores)
print(valores)
