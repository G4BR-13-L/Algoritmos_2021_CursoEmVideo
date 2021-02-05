# coding=utf-8
'''
25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
de cada lado deve ser menor que a soma dos outros dois.
'''

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if ((r1<=(r2+r3)) and (r2<=(r1+r3)) and (r3<=(r1+r2))):
    print('É possivel fazer um triangulo.')
else:
    print('Não é possivel fazer um tringulo com essas retas!')