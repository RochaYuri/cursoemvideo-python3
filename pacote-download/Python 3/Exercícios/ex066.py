cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    # a SOMA e a CONTAGEM devem vir depois do break para não contar/somar o flag, que
    # deve interromper o loop com o BREAK
    cont += 1
    soma += n
print(f'Você digitou {cont} números.')
print(f'A soma é {soma}.')
