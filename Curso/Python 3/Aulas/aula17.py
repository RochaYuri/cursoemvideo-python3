num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores1 = []
valores1.append(5)
valores1.append(9)
valores1.append(4)

for c, v in enumerate(valores1):
    print(f'Na posição {c} encontrei o número {v}!')
print('Cheguei ao final da lista!')

valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o número {v}!')
print('Cheguei ao final da lista!')
