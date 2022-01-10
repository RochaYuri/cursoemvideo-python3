preco = float(input('Digite o preco do produto: R$'))
print('''[ 1 ] = A vista Dinheiro/Cheque (10% de desconto)
[ 2 ] = A vista Cartao (5% de desconto)
[ 3 ] = Em ate 2x no Cartao (Preco normal)
[ 4 ] = 3x ou mais no Cartao (20% de juros)''')
tipo = int(input('Escolha a opcao de pagamento: '))
if tipo == 1:
    total = preco * 0.9
elif tipo == 2:
    total = preco * 0.95
elif tipo == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS!')
elif tipo == 4:
    quantparc = int(input('Quantas parcelas? '))
    total = preco * 1.2
    if quantparc >= 3:
        parcela = total / quantparc
        print(f'Sua compra será parcelada em {quantparc}x de R${parcela:.2f} COM JUROS!')
    else:
        print('O limite mínimo de parcelas é 3! Escolha novamente a quantidade de parcelas!')
else:
    total = preco
    print('OPCAO INVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE!')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final!')
