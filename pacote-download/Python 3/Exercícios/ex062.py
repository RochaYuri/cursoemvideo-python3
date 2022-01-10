a = int(input('Digite o primeiro termo da P.A: '))
b = int(input('Digite a razão da P.A: '))
c = int(input('Digite a quantidade de termos da P.A: '))
d = a
while d != (a+(b*c)):
    print(f'{d} → ', end='')
    d += b
print('PAUSA')
x = 1
while x != 0:
    x = int(input('Quantos termos você quer mostrar a mais? '))
    while d != (a+(b*(c+x))):
        print(f'{d} → ', end='')
        d += b
    c += x
    if x != 0:
        print('PAUSA')
print(f'Progressão finalizada com {((d-a)/b):.0f} termos mostrados.')
