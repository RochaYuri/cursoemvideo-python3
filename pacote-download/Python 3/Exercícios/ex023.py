n = input('Escreva um número de 0 até 9999 ')
v = ('{:>4}'.format(n))
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(v[3], v[2], v[1], v[0]))
