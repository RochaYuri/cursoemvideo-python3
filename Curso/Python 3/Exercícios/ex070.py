print('Lojão o Baratão')
print(30*'-')
barato=soma=cont=0
while True:
    produto = str(input('Nome do Produto :'))
    preco = float(input('Preço R$ :'))
    resp=str(' ')
    soma+=preco
    if preco < barato or barato==0:
        barato=preco
        prod=produto.upper()
    if preco > 1000:
        cont+=1
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp in 'Nn':
        print('---------FIM DO PROGRAMA-----------')
        break
print(f'O total da compra foi {soma}\nTemos {cont} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {prod} e custou R$ {barato:.2f}')
