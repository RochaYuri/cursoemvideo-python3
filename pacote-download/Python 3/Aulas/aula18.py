teste = []
teste.append('Yuri')
teste.append(22)
galera = []
galera.append(teste[:])                      # A CÓPIA É IMPORTANTE POIS SEM ELA AS ESTRUTURAS SÃO AFETADAS EM CONJUNTO
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])                      # OUTRA CÓPIA
print(galera)

#+============================================================================

# POSIÇÕES ->     0            1               2              3
#              0     1      0     1        0       1       0      1
galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera1[2][1])
for p in galera1:
    print(f'{p[0]} possui {p[1]} anos de idade.')

#=============================================================================

#RECEBENDO INFORMAÇÕES DENTRO DE UMA LISTA, PARA COMPOR A OUTRA

galera2 = []
dados = []
totmaior = totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera2.append(dados[:])
    dados.clear()
print(galera2)

for p in galera2:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')
