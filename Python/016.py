# coding=utf-8
'''
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.
'''

cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))

vidaNoLixo = float((((cigarros*10)*(anos*365))/60)/24);

print('Já se foram {:.2f} dias de vida' .format(vidaNoLixo))