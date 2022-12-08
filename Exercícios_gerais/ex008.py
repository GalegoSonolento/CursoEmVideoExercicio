medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10

print('{} metros valem \n {} centímetros e \n {} milímetros'.format(medida, cm, mm))
print('Além disso, também vale: \n {}km, \n {}hm, \n {}dam, \n {}dm'.format(km, hm, dam, dm))