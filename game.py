from player import Player
from shop import Shop
from textTools import *
import random

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
                self.fight()
            else:
                marqueeprint("Did you do preparations, young grasshopper?")

    def fight(self):
        while playerOne.isAlive() and playerTwo.isAlive():
            playerOne.hp = fightTurn(playerOne, playerTwo)
            centerprint("{} HP [{}]".format(playerOne.name, str(| * (playerOne.hp // 10))))
            fightTurn(playerTwo, playerOne)
            centerprint("{} HP [{}]".format(playerTwo.name, str(| * (playerTwo.hp // 10))))
        if playerOne.hp < 0:
            marqueeprint("PLAYER TWO WINS!")
            return
        else:
            marqueeprint("PLAYER ONE WINS!")
            return

    def fightTurn(self, x, y):
        marqueeprint(x.name + "'s Turn")
        centerprint('[a]ttack - [s]kill - [p]otion')
        move = input()
        if move == 'a' or move == '':
            y.takeDamage(x.atk)
            centerprint("{} attacks {} for {} damage!".format(x.name, y.name, str(x.atk)))
            return x.hp
        elif move == 's':
            if x.ourClass == 'Arcstrider':
                y.hp = y.hp / 2
                return x.hp
            elif x.ourClass == 'Dawnblade':
                x.takeDamage(50)
                return x.hp
            elif x.ourClass == 'Gunslinger':
                amt = 0
                y.takeDamage(x.atk)
                amt += x.atk
                y.takeDamage(x.atk)
                amt += x.atk
                centerprint("{} attacks {} twice for {} damage".format(x.name, y.name, str))
            elif x.ourClass == 'Sentinel':
                y.takeDamage(x.atk + y.defn)
                centerprint("{} goes through {}'s defense and attacks for {} damage".format(x.name, y.name, x.atk + y.defn))
            elif x.ourClass == 'Voidwalker':
                x.hp += y.atk
                centerprint("{} dodges {}'s attack".format(x.name, y.name))
            else:
                # TODO ADD A SKILL COUNTER (2). IF IT'S 0, THEN YOU CAN'T USE YOUR SKILL
                # TODO ADD COLORS
                p = random.random() * 100
                if p <= 20:
                    amt = y.hp // 4
                    y.hp = amt
                    x.hp = x.hp + amt
                    centerprint('{} initiates LIFESTEAL!'.format(x.name))
                    return
                else: 
                    centerprint(self.RED + self.BOLD + "MISSED" + self.END)
                    return




    def printPlayer(self, player):
        marqueeprint(sometext)
        print(lr_justify('[Player]', '', self.textwidth))
        print(lr_justify(self.playerOne.name, '', self.textwidth))
        print(lr_justify(str('lvl: ' + str(self.ourhero.level)), '', self.textwidth))
        print(lr_justify(str('HP: ' + str(self.ourhero.hp) + '/' + str(self.ourhero.maxhp)), '', self.textwidth))
        print(lr_justify(str('XP: ' + str(self.ourhero.xp) + '/' + str(self.ourhero.nextlevel)), '', self.textwidth))
