# https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html



print('Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.')
lista = [1,2,3,4]

quadrados = []
for n in lista:
    valor = n **2
    quadrados.append(valor)

print(quadrados)