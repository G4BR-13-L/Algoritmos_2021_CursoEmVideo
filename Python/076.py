# coding=utf-8
from random import randint
array = []
cont = 0

while cont <= 7:
    array.append(randint(0,100))
    cont += 1
else:
    print("Numeros Gerados com sucesso! \n{} \nFim da execução!" .format(array))


