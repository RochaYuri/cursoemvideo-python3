maior = homem = mulher = 0
#continua = 'S' # para substituir pelo BREAK no final do código
 (Famosa GAMBIARRA) KKKK...
print('{:=^33}'.format('INICIO DO PROGRAMA'))
while True:
#while continua == 'S': # substituido pelo BREAK no final do código
    print('-'*33)
    print('{:-^33}'.format(' * CADASTRE UMA PESSOA * '))
    print('-'*33)
    idade = int(input('Digite a idade! '))
    if idade > 18:
        maior += 1
    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('Digite o sexo! [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    continua = ' '
    print('-'*33)
    while not continua in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-'*33)
    if continua == 'N':
        break
print('{:=^33}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoa(s) com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homen(s) cadastrado(s)')
print(f'E temos uma {mulher} com menos de 20 anos')
print('fim da execução')
