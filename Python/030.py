# coding=utf-8
'''
30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
'''

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if ((r1<=(r2+r3)) and (r2<=(r1+r3)) and (r3<=(r1+r2))):
    print('É possivel fazer um triangulo.')
    if r1 == r2 == r3:
        print('O trinagulo resultante é equlátero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
	    print('O triangulo resultante é isóceles')
    else:
        print('O triangulo resultante é escaleno.')
else:
    print('Não é possivel fazer um tringulo com essas retas!')