# COMANDOS IMPORTADOS:

from random import randint
from time import sleep

# MENSAGEM TÍTULO:

titulo = 'PAR OU ÍMPAR!'

# APRESENTAÇÃO DO TÍTULO:

print('=' * 60)                         # apresenta linha de abertura
print('{:^60}'.format(titulo))          # apresenta título formatado
print('-' * 60)                         # apresenta linha divisória

# INTERAÇÃO COM O USUÁRIO:

# VARIANTES INICIAIS:               # variantes necessárias para a ação principal

count = win = 0
luck = ''

# AÇÃO PRINCIPAL:                   # ação que satisfaz o enunciado

while True:
    player = int(input('Digite um número inteiro de 0 a 10:   '))
    choice = str(input('A soma será par ou ímpar [P/I]        ')).strip().upper()[0]
    comput = randint(0,10)

    sum = comput + player
    count = count + 1
    sleep(1)
    print(f'O computador jogou {comput}')

    if sum % 2 == 0:
        luck = 'Pp'
        print(f'A soma foi {sum} e é [par].')
    elif sum % 2 != 0:
        luck = 'IÍ'
        print(f'A soma foi {sum} e é [ímpar].')
    if choice in luck:
        win = win + 1
        print(f'\033[1;34mParabéns você venceu mais esta {count}a jogada!\033[m')
        print(60 * '+')
    else:
        break
if win > 0:
    print(f'Parabéns, você venceu {win} jogadas!')
print('\033[1;31mPara mais jogadas, reinicie!\033[m')

print('-' * 60)                       #apresenta linha divisória

# FECHAMENTO:

print('-' * 60)                       #apresenta linha divisória
print('=' * 60)                     #apresenta linha divisória
print('\n')                         #apresenta linha vazia
