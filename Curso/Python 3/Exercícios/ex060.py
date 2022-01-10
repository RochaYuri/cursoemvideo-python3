contador = 1
numero = int(input('Digite um numero para fatorar: '))
while numero >= 1:
    contador *= numero
    numero = numero - 1
print(contador)
