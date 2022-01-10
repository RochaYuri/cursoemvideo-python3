num = int(input('Digite um número para ver sua tabuada:'))
for p in range(1, 11):
    print('{} x {} = {}'.format(num, p, num * p))
