velocidade = float(input('Qual é a velocidade atual do seu carro?'))
maxima = (velocidade-80)*7
if velocidade <= 80:
  print('Dirija com atenção')
else:
  print('Sua velocidade foi {:.0f} e receberá uma multa de {:.2f}'.format(velocidade, maxima))
