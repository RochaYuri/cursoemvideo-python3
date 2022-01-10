sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Por favor digite a letra correta!!!')
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

print('O sexo escolhido foi: {}'.format(sexo))
