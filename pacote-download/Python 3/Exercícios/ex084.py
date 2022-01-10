galera = []
dados = []
mai = men = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(dados) == 0:
        mai = menor = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    galera.append(dados[:])

    dados.clear()

    r = str(input('Quer continuar? [S/N] ')).upper().split()

    if 'N' in r:
        break

print('=-'*25)

print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi de {mai}KG.')
print(f'O menor peso foi de {men}KG.')
