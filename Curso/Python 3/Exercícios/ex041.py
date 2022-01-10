"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
from datetime import date
current_year = date.today().year
birth_year = int(input('Informe seu ano de nascimento: '))
age = current_year - birth_year
print('No momento você está com {} anos. \nVamos verificar qual categoria você se encaixa.'.format(age))
print('-' * 25)
if 0 < age <= 9:
    print('MIRIM')
elif 10 < age <= 14:
    print('INFANTIL')
elif 15 < age <=19:
    print('JÚNIOR')
elif 20 < age <= 25:
    print('SÊNIOR')
elif age > 26:
    print('MASTER')
else:
    print('ERRO 404 - Tente Novamente')
print('-' * 25)
