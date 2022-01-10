a = int(input('digite um valor '))
b = int(input('digite um valor '))
c = int(input('digite um valor '))
if a == b and b == c:
    print('haha todos os numeros sao iguais')
else:
    if a > b and a > c:
        print('detre o número {}, {} e {}, o maior número é {}'.format(a, c, b, a))
    else:
        if b > a and b > c:
            print('dentre os números {}, {} e {}, o maior número é {} '.format(a, b, c, b))
        else:
            print('dentre todos os números {}, {} e  {}  é o maior deles é {}'.format(a, b, c, c))
