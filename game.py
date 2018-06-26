from player import Player
from shop import Shop
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
        centerprint("Press Enter to Play")
        print("")
        enter = input()
        if enter == '' or enter == 'e' or enter == 'E':
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
                    self.fight()
        else:
            return


    def newPlayer(self, person):
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
            centerprint("Lazy")
            ourClass = 'Warlock'
        # ------------Name---------- #
        marqueeprint('[ENTER NAME]')
        centerprint('Your name, ' + str(ourClass) + '?\n')
        name = input()
        if len(name) == 0:
            name = 'Sir Lazy'
            
        player = Player(ourClass, name)
        return player


    def fight(self):
        while self.playerOne.hp > 0 and self.playerTwo.hp > 0:
            if self.playerOne.hp == 200:
                self.playerOne.hp = 160
            elif self.playerTwo.hp == 200:
                self.playerTwo.hp = 160
            healthList = []
            health = (self.fightTurn(self.playerOne, self.playerTwo))
            healthList.append(health[0])
            healthList.append(health[1])
            self.playerOne.hp = health[0]
            self.playerTwo.hp = health[1]
            centerprint(str(self.playerOne.name) + "HP: " + str(self.playerOne.hp))
            centerprint(str(self.playerTwo.name) + "HP: " + str(self.playerTwo.hp))
            health = (self.fightTurn(self.playerTwo, self.playerOne))
            healthList.append(health[0])
            healthList.append(health[1])
            self.playerTwo.hp = health[0]
            self.playerOne.hp = health[1]
            centerprint(str(self.playerOne.name) + "HP: " + str(self.playerOne.hp))
            centerprint(str(self.playerTwo.name) + "HP: " + str(self.playerTwo.hp))
        if self.playerOne.hp < 0:
            marqueeprint("")
            marqueeprint("PLAYER TWO WINS!")
            self.endLoop = True
            return
        elif self.playerTwo.hp < 0:
            marqueeprint('')
            marqueeprint("PLAYER ONE WINS!")
            self.endLoop = True
            return

    def fightTurn(self, x, y):
        print('')
        marqueeprint(x.name + "'s Turn")
        centerprint('[a]ttack - [s]kill')
        move = input()
        if move == 'a' or move == '':
            y.takeDamage(x.atk - y.defn)
            centerprint("{} attacks {} for {} damage!\n".format(x.name, y.name, str(x.atk - y.defn)))
            return [x.hp , y.hp]
        elif move == 's':
            p = random.random() * 100
            if x.ourClass == 'Arcstrider':
                if p <= 20:
                    y.hp = y.hp / 2
                    return [x.hp , y.hp]
                else:
                    self.missed()
                    return [x.hp , y.hp]
            elif x.ourClass == 'Dawnblade':
                if p <= 60:
                    x.takeDamage(50)
                    centerprint('{} takes 50 recoil damage'.format(x.name))
                    return [x.hp , y.hp]
                elif p > 60:
                    x.atk += 40
                    centerprint('{} boosts attacks for one turn'.format(x.name))
                    return [x.hp , y.hp]
                else:
                    self.missed()
                    return [x.hp , y.hp]
            elif x.ourClass == 'Gunslinger':
                if p <= 50:
                    amt = 0
                    y.takeDamage(x.atk - y.defn)
                    amt += x.atk
                    y.takeDamage(x.atk - y.defn)
                    amt += x.atk
                    centerprint("{} attacks {} twice for {} damage".format(x.name, y.name, str(amt)))
                    return [x.hp , y.hp]
                else:
                    self.missed()
                    return [x.hp , y.hp]
            elif x.ourClass == 'Sentinel':
                if p <= 99:
                    y.takeDamage(x.atk + y.defn)
                    centerprint("{} goes through {}'s defense and attacks for {} damage".format(x.name, y.name, x.atk + y.defn))
                    return [x.hp , y.hp]
                else:
                    self.missed()
                    return [x.hp , y.hp]
            elif x.ourClass == 'Voidwalker':
                if p <= 30:
                    x.hp += y.atk
                    centerprint("{} dodges {}'s attack".format(x.name, y.name))
                    return [x.hp , y.hp]
                else:
                    self.missed()
                    return [x.hp , y.hp]
            else:
                # TODO ADD A SKILL COUNTER (2). IF IT'S 0, THEN YOU CAN'T USE YOUR SKILL
                # TODO ADD COLORS
                if p <= 20:
                    amt = y.hp // 4
                    y.hp = amt
                    x.hp = x.hp + amt
                    centerprint('{} initiates LIFESTEAL!'.format(x.name))
                    return x.hp
                else: 
                    self.missed()
                    return [x.hp , y.hp]
            
        else:
            centerprint("Invalid selection")
            


    def missed(self):
        centerprint(self.RED + self.BOLD + "MISSED" + self.END)

    def printPlayer(self, player):
        # marqueeprint(sometext)
        print(lr_justify('[Player]', '', self.textwidth))
        print(lr_justify(player.name, '', self.textwidth))
        print(lr_justify(str('HP: ' + str(player.hp) + '/' + str(player.maxhp)), '', self.textwidth))

test = Game()
test.gameloop()
