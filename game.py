from player import Player
from shop import Shop
from textTools import *

class Game():

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

    def __init__(self):

        self.playerOne = 0
        self.playerTwo = 0

        self.oneTurn = False
        self.twoTurn = False

        self.mistakeCounter = 0

        self.textwidth = 70

        self.didPreparations = False


    def newPlayer(self, person):
        # -----------Class-----------#
        marqueeprint(person + ' - [CHOOSE CLASS]')
        centerprint('[a]rcstrider [d]awnblade [g]unslinger [s]entinel [v]oidwalker [w]arlock')
        ourClass = input()
        if ourClass == 'a':
            ourClass = 'Arcstrider'
        elif ourClass == 'd':
            ourClass = 'Dawnblade'
        elif ourClass == 'g':
            ourClass = 'Gunslinger'
        elif ourClass == 's':
            ourClass = 'Sentinel'
        elif ourClass == 'v':
            ourClass = 'Voidwalker'
        elif ourClass == 'w':
            ourClass = 'Warlock'
        else:
            centerprint('Please enter a valid selection')
            ourClass = input()
        # ------------Name---------- #
        marqueeprint('[ENTER NAME]')
        centerprint('Your name, ' + str(ourClass) + '?\n')
        name = input()
        if name == '':
            name = 'Sir Lazy'

        player = Player(ourClass, name)
        return player


    def gameloop(self):
        while True:
            marqueeprint('')
            centerprint('Kombat RPG')
            centerprint('Game Design 1 - 2018')
            marqueeprint('')
            centerprint('[p]reparation [f]ight')
            decision = input()
            if decision == 'p' or decision == '':
                self.didPreparations = True
                self.playerOne = self.newPlayer()
                self.playerTwo = self.newPlayer()
                self.playerOne.playerPerks()
                self.playerOne.datadict()
            if decision == 'l' and self.didPreparations:
                print('LOADING BATTLE GROUNDS')
                self.ourhero = self.loadgame()
                self.ourenemy = self.getenemy()
            else:
                marqueeprint("Did you do preparations, young grasshopper?")
            while self.ourhero.isalive():
                self.fight()



    def printPlayer(self, player):
        marqueeprint(sometext)
        print(lr_justify('[Player]', '', self.textwidth))
        print(lr_justify(self.playerOne.name, '', self.textwidth))
        print(lr_justify(str('lvl: ' + str(self.ourhero.level)), '', self.textwidth))
        print(lr_justify(str('HP: ' + str(self.ourhero.hp) + '/' + str(self.ourhero.maxhp)), '', self.textwidth))
        print(lr_justify(str('XP: ' + str(self.ourhero.xp) + '/' + str(self.ourhero.nextlevel)), '', self.textwidth))
