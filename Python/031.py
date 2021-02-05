# coding=utf-8
'''
31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
'''
from random import randint
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print(color.BOLD + color.GREEN + 'Pedra Papel e tesoura \n' + color.END)
usrPoints = 0
pythonPoints = 0
weapons = ['Pedra', 'Papel', 'Tesoura']
repeater = 0
while repeater != 1:
    usrWeapon = int(input('0 = pedra \n1 = papel \n2 = tesoura \n\n'))
    pythonWeapon = int(randint(0,2))
    if(((usrWeapon == 0) and (pythonWeapon == 2)) or ((usrWeapon == 1) and (pythonWeapon == 0)) or ((usrWeapon == 2) and (pythonWeapon == 1))):
        usrPoints += 1
        usrwin = True
        pywin = False
    else:
        pythonPoints += 1
        pywin = True
        usrwin = False
    print('Usuário: {} \nPython: {} \n' .format(weapons[usrWeapon], weapons[pythonWeapon]))
    if usrwin == True:
        print(color.BOLD + color.CYAN + 'Você venceu!!' + color.END)
    elif pywin == True:
        print(color.BOLD + color.YELLOW + 'Python venceu!!' + color.END)
    repeater = input(color.BOLD + color.RED + 'Para finalizar o jogo pressione 1:    ' + color.END)
    if repeater == 1:
        print(color.BOLD + color.BLUE + 'PONTUAÇÃO \n' + color.END)
        print('Usuário: {}\nPython: {}' .format(usrPoints, pythonPoints))







