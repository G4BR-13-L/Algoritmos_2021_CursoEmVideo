# coding=utf-8
'''
3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
'''

nome = input('Qual o nome do funcionário? ')
salario = float(input('Qual o salário do funcionário? '))
print('Nome do funcionário: {} \nSalário: {} \n O funcionário {} tem um salário de R${} em Junho.' .format(nome, salario, nome, salario))
