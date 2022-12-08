larg = float(input('Dê a largura da parede: '))
alt = float(input('Dê a aultura da parede: '))
area = larg * alt
print('Sua parede tem dimensões {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar toda a parede, você precisa de {}l de tinta'.format(tinta))