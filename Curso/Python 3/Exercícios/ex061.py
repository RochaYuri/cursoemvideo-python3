n1 = int(input('Valor do primero termo: '))
r = int(input('Valor da razão: '))
n10 = n1 +(10-1)*r
n = 10
a=0
print(n10)
print(f'Os 10 primeros termo da P.A de razão {r} e o primero termo {n1}')
while a!= n10:
    a = n1 + (10-n)*r
    n=n-1
    print(a,end=',' if a != n10 else '...')
print('\nEnd.')
