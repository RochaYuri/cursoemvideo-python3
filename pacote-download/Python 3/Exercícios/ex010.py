real = float(input('Quanto você tem de dinheiro na sua carteira? R$'))
dolar = real / 5.23
euro = real / 6.37
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(real, euro))
