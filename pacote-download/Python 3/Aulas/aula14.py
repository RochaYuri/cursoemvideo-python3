num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um número inteiro: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pars e {} números ímpares.'.format(par, impar))
