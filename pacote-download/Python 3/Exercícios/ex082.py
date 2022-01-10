complete = []
par = []
impar = []
cont = 0

print("=" * 50)  # FIRULAS 1

while True:
    num = int(input("Digite um número: "))
    cont += 1
    complete.append(num)
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    while resp not in "SN":
        print("Opção inválida! Tente novamente.")
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        for v in complete:
            if v % 2 == 0:
                par.append(v)
            else:
                impar.append(v)
        break

print("=" * 50)  # FIRULAS 2

print(f"A lista completa é: {complete}")
if len(par) <= 0:
        print("Você não atribuiu valores pares à lista.")
else:
    if len(par) > 0:
        print(f"A lista com valores pares é: {par}")
if len(impar) <= 0:
        print("Você não atribuiu valores impares à lsita.")
else:
    if len(impar) > 0:
        print(f"A lista com valores impares é: {impar}")

print("=" * 50)  # FIRULAS 3
