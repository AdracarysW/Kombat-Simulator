from player import Player
from textTools import *
import random
import time

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
        self.justFight = False

        self.endLoop = False

        self.something = False

    def gameloop(self):
        marqueeprint('')
        centerprint('Kombat RPG')
        centerprint('Game Design 1 - 2018')
        marqueeprint('')
        print("")
        centerprint("Press Any Key to Play")
        print("")
        enter = input()
        if enter == '' or len(enter) > 0:
            while True:
                if self.endLoop:
                    return
                if not(self.didPreparations):

                    self.didPreparations = True
                    self.playerOne = self.newPlayer('Player One')
                    self.playerTwo = self.newPlayer('Player Two')
                    self.playerOne.playerPerks()
                    self.playerTwo.playerPerks()

                else:    
                    self.simulation()
                    self.fight()
        else:
            return


    def simulation(self):
        i = 1
        while i <= 2:
            centerprint('LOADING BATTLE GROUNDS' + ('.' * i))
            time.sleep(1)
            i += 1
        centerprint('BATTLE GROUNDS LOADED')
        time.sleep(1)
        print('')
        marqueeprint('FIGHT')
        print('')

    def newPlayer(self, person): # Making a new player
        # -----------Class-----------#
        marqueeprint(person.upper() + ' - [CHOOSE CLASS]')
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
            centerprint("Lazy\n")
            ourClass = 'Warlock'
        # ------------Name---------- #
        marqueeprint('[ENTER NAME]')
        centerprint('Your name, ' + str(ourClass) + '?\n')
        name = input()
        if len(name) == 0:
            name = 'Sir Lazy'
            centerprint("Sir Lazy")
        #----Creating new player----#    
        player = Player(ourClass, name)
        return player


    def fight(self): # Players fight here
        while self.playerOne.isAlive() and self.playerTwo.isAlive():
            self.checkAbilities()
            self.fightTurn(self.playerOne, self.playerTwo)
            self.printHp()
            self.fightTurn(self.playerTwo, self.playerOne)
            self.printHp()
        self.checkWinner()

    def checkAbilities(self):
        pass

    def checkWinner(self): # Checks for winner 
        if not self.playerOne.isAlive():
            print("")
            marqueeprint(self.playerTwo.name + ' wins!')
            self.endLoop = True
            return
        elif not self.playerTwo.isAlive():
            print('')
            marqueeprint(self.playerOne.name + ' wins!')
            self.endLoop = True
            return

    def printHp(self):
        centerprint('{} HP: {}/{}'.format(self.playerOne.name, str(self.playerOne.hp), str(self.playerOne.maxHp)))
        centerprint('{} HP: {}/{}'.format(self.playerTwo.name, str(self.playerTwo.hp), str(self.playerTwo.maxHp)))

    def fightTurn(self, x, y):
        cost = 1
        print('')
        marqueeprint(x.name + "'s Turn")
        centerprint('[a]ttack - [s]kill')
        move = input()
        if move == 'a' or move == '':
            y.takeDamage(x.atk - y.defn)
            centerprint("{} attacks {} for {} damage!\n".format(x.name, y.name, str(x.atk - y.defn)))
        elif move == 's':
            p = random.random() * 100
            if x.ourClass == 'Arcstrider' and x.enoughMana(cost):
                if p <= 25:
                    amt = y.hp / 2
                    y.hp = amt
                    centerprint("{} deals critcial damage and halves {}'s health by {}".format(x.name, y.name, amt))
                else:
                    self.missed()
            elif x.ourClass == 'Dawnblade' :
                if p <= 60:
                    x.takeDamage(50)
                    centerprint('{} takes 50 recoil damage'.format(x.name))
                elif p > 60:
                    x.atk += 40
                    centerprint('{} boosts attacks for one turn'.format(x.name))
                else:
                    self.missed()
            elif x.ourClass == 'Gunslinger':
                if p <= 50:
                    amt = 0
                    y.takeDamage(x.atk - y.defn)
                    amt += x.atk
                    y.takeDamage(x.atk - y.defn)
                    amt += x.atk
                    centerprint("{} attacks {} twice for {} damage".format(x.name, y.name, str(amt)))
                else:
                    self.missed()
            elif x.ourClass == 'Sentinel':
                if p <= 90:
                    y.takeDamage(x.atk)
                    centerprint("{} goes through {}'s defense and attacks for {} damage".format(x.name, y.name, x.atk + y.defn))
                else:
                    self.missed()
            elif x.ourClass == 'Voidwalker':
                if p <= 30:
                    x.hp += y.atk
                    centerprint("{} gains health equal to {}'s attack for {} HP".format(x.name, y.name, y.atk))
                else:
                    self.missed()
            else:
                if p <= 27:
                    amt = y.hp // 4
                    y.hp = amt
                    x.hp = x.hp + amt
                    centerprint('{} initiates LIFESTEAL!'.format(x.name))
                else: 
                    self.missed()
            
        else:
            centerprint("Invalid selection")

        if self.playerOne.name == x.name:
            self.playerOne.hp = x.hp
            self.playerTwo.hp = y.hp
        else:
            self.playerOne.hp = y.hp
            self.playerTwo.hp = x.hp
        
        
            


    def missed(self):
        centerprint(self.RED + self.BOLD + "MISSED" + self.END)

    def printPlayer(self, player):
        # marqueeprint(sometext)
        print(lr_justify('[Player]', '', self.textwidth))
        print(lr_justify(player.name, '', self.textwidth))
        print(lr_justify(str('HP: ' + str(player.hp) + '/' + str(player.maxhp)), '', self.textwidth))

test = Game()
test.gameloop()
