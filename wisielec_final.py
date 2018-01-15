from os import system
from time import sleep
from sys import argv
from random import choice
from sys import version_info as ver
from platform import system as os


def print_gallows(n):
    body = ['/','|','(_)','\\|','/','|','/','\\']
    current_body = ['','','','','','','','']
    for i in range(len(body)):
        if i<n: current_body[i] = body[i]
      
    print("""
            ______
            |%s%s
            |%s
            |%s%s
            | %s
            |%s%s
        """ % tuple(current_body))


def print_interface(guess):
    shoots = set()
    lines=''
    fails = 0
    
    for i in guess:
        if not i == ' ':
            lines+='-'
        else:
            lines+=' '
    print('Uzyte: ')
    print( [i for i in shoots] )
    print('Haslo: ')
    print(lines)
    print_gallows(fails)

    while True:
        if ver.major == 2:
            # python2
            letter = raw_input(">> ")
        else:
            # python3
            letter = input(">> ")

        failed = True
        
        if letter in shoots:
            failed = False
        else:
            shoots.add(letter)

        clear()	
        
        lines = ''
        for i in guess:
            if not i == ' ':
                if i in shoots:
                    lines+=i
                    if i == letter: failed = False
                else:
                    lines+='-'
            else:
                lines+=' '
                
        print('Uzyte: ')
        print( [i for i in shoots] )
        print('Haslo: ')
        print(lines)
        
        if failed: fails+=1
        print_gallows(fails)
        
        if fails == 8:
            return False
        if '-' not in lines:
            return True


def read_modules(file):
    modules = set()
    try:
        f = open(file, 'r')
    except IOError:
        print('Nie ma takiego pliku.')
        return False
    else:
        for line in f:
            modules.add(line[:-1])
        return modules

     
def game_start(modules):
    guess = choice(tuple(modules))
    if print_interface(guess):
        print('Brawo! Wygrales xD')
    else:
        print('UUU. Przegrales :(')


standard_modules = [
                    'galaretka',
                    'python',
                    'kot',
                    'student',
                    'nokia',
                    'sesja',
                    'pierogi',
                    'delikwent'
                    ]

medium_modules = [
                  'mordercza kaczka',
                  'noga biednego dziadka',
                  'jasny pantofel kopciuszka',
                  'czerwony maluch',
                  'trudne kolokwium u tofika',
                  'zimna zima',
                  'babie lato',
                  'gotowanie kartofli',
                  'ciemna strona mocy',
                  'jasny poziom monitora'
                  ]

hard_modules = [
                'wielki nos jak u pinokia',
                'zderzaki na starym aucie',
                'nokia jest bardzo fajna',
                'programista to cwana osoba',
                'wiele rzeczy jest w przestrzeni'
                ]

def clear():
    if os() == 'Windows':
        system('cls')
    elif os() == 'Linux':
        system('clear')


if __name__ == '__main__':
    clear()
    print("Witaj w grze w wisielca!")
    print("Skrypt napisany na PAWO - nokie!")
    print("Autor Jacek Piszczek")
    sleep(1)
    clear()
    
    if len(argv) == 3 and argv[1] == 'file':
        modules = read_modules(argv[2])
        if not modules:
            modules = standard_modules
            print('Nie wczytano pliku. Ladowanie easy poziomu.')
            sleep(2)
    elif len(argv) == 2:
        if argv[1] == 'easy': modules = standard_modules
        elif argv[1] == 'medium': modules = medium_modules
        elif argv[1] == 'hard': modules = hard_modules
        else:
            modules = standard_modules
            print('Nie ma takiego poziomu. Ladowanie easy poziomu.')
            sleep(2)
    else:
        modules = standard_modules
        print('Cos zle podales. Ladowanie easy poziomu.')
        sleep(2)
        
    clear()
    game_start(modules)
