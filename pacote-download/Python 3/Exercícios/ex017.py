import math
cat1 = int(input('Digite o comprimento do primeiro cateto: '))
cat2 = int(input('Digite o comprimento do segundo cateto: '))
res = math.hypot(cat1, cat2)
print('A Hipotenusa desse triângulo-retângulo será {}'.format(res))
