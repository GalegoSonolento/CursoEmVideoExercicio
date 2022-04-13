peso = float(input('Qual seu pseo? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('Você está com O PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado redobrado')
