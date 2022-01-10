valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))

prestacao = valorCasa / (tempo*12)


print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorCasa, tempo, prestacao))


if prestacao > (salario * 0.3):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
