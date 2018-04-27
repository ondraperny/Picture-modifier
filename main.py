# Python semestral work

import sys
sys.excepthook = sys.__excepthook__
import os
import numpy as np
from PIL import Image
# clear display
print('\033[2J', end='')


def rotateRight():
    pass


def rotateLeft():
    pass


def mirror():
    pass


def invert():
    pass


def greyscale():
    pass


def lighten():
    pass


def darken():
    pass


def highlightEdge():
    pass

def loadInput():
    print('\033[2J')
    file = input('Zadejte jméno souboru:\n')
    while os.access(file, os.R_OK) == False:
        print('\033[2J', end='')
        print('Zadaný soubor nelze načíst, zadejte jiný:')
        file = input('Zadejte jméno souboru:\n')
    print('\033[2J', end='')
    fileData = np.array(Image.open(file))
    return file, fileData

def saveOutput(fileData, file, change):
    f = Image.fromarray(fileData, 'RGB')
    f.save(change + "_" + file + ".png")

flag = 0
# interface
print('Program pro upravu obrazku, zadej jmeno souboru, ktery chces upravit: ')
# file, fileData = loadInput()
file, fileData = 'test.png', np.array(Image.open('test.png'))

while True:
    if flag == -1:
        print('Špatný výběr, volte znovu')
    else:
        print()

    print('Aktuální soubor: \"' + file + '\"' )
    print('''Seznam možností (vyber číslo a stiskni enter):
          0. exit - vypne program
          1. nový soubor - nechá uživatele zadat nový soubor
          2. rotace do prava o 90 stupňů
          3. rotace do leva o 90 stupňů
          4. zrcadlení obrazu
          5. inverze obrazu
          6. převod do odstínu šedi
          7. zesvětlení
          8. ztmavení
          9.zvýraznění hran''')
    flag = input()
    if flag == '0':
        print('\033[2J', end='')
        exit()
    elif flag == '1':
        file, fileData = loadInput()
    elif flag == '2':
        rotations = int(input('Kolikrát chceš obrázek pootočit? (Zadej číslo): '))
        fileData = np.rot90(fileData, -rotations)
        saveOutput(fileData, file, "rotateRight")
    elif flag == '3':
        rotations = int(input('Kolikrát chceš obrázek pootočit? (Zadej číslo): '))
        fileData = np.rot90(fileData, rotations)
        saveOutput(fileData, file, "rotateLeft")
    elif flag == '4':
        fileData = np.flip(fileData, 1)
        saveOutput(fileData, file, "mirror")
    elif flag == '5':
        fileData[::] = 255 - fileData[::]
        saveOutput(fileData, file, "invert")
    elif flag == '6':
        for i in range(len(fileData)):
            for j in range(len(fileData[0])):
                fileData[i][j][:] = np.dot(fileData[i][j][:], [0.299, 0.587, 0.114]).sum()
        saveOutput(fileData, file, "greyscale")
    # elif flag == '7':
    # elif flag == '8':
    # elif flag == '9':
    else:
        flag = -1
    print('\033[2J', end='')

