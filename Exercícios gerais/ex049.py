num = int(input('Digite um número para realizar a tabuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))
