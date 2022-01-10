nofwomens = 0
nmoreold = ''
moreold = 0
somaid = 0
for c in range(1, 6):
    print('========== {}° Pessoa =========='.format(c))
    nome = str(input('>>Nome: '))
    idade = int(input('>>Idade: '))
    gen = str(input('>> Gênero [F/M]: ')).strip().lower()
    somaid += idade
    if gen == 'f' and idade < 20:
        nofwomens += 1
    if c == 1:
        moreold = idade
        nmoreold = nome
    if idade > moreold:
        moreold = idade
        nmoreold = nome
mediaid = somaid / 5
print('='*31, '\n>>A média de idade desse grupo de pessoas é de {} anos.'.format(mediaid))
print('>>A pessoa mais velha deste grupo tem {} anos e se chama {}.'.format(moreold, nmoreold))
print('>>Ao todo são {} mulheres com menos de 20 anos.'.format(nofwomens))
