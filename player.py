
from textTools import *
from description import *

class Player():

    def __init__(self, playerClass, name):
        self.ourClass = playerClass
        self.name = name
        self.mana = 3
        self.hp = 0
        self.maxHp = 0
        self.atk = 0
        self.spd = 0
        self.defn = 0
        self.mana = 0
        self.gold = 100
        self.dataWidth = 40

    def characters(self):
        print(description)

    def getName(self):
        return self.name

    def buyitem(self, item):
        if self.canAfford(item):
            self.gold -= item
            self.items.append(item)
            print('You bought ' + item)
        else:
            print('You can\'t afford that!')

    def canAfford(self, val):
        if self.gold >= val:
            return True
        else:
            return False

    def enoughMana(self, val):
        if self.mana >= val:
            return True
        else:
            return False

    def isAlive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def takeDamage(self, amount):
        self.hp -= amount

    def playerPerks(self):
        if self.ourClass == 'Arcstrider':
            self.hp = 300
            self.maxHp = 300
            self.atk = 90
            self.spd = 60
            self.defn = 50
        elif self.ourClass == 'Dawnblade':
            self.hp = 450
            self.maxHp = 450
            self.atk = 160
            self.spd = 20
            self.defn = 20
        elif self.ourClass == 'Gunslinger':
            self.hp = 330
            self.maxHp = 330
            self.atk = 80
            self.spd = 50
            self.defn = 40
        elif self.ourClass == 'Sentinel':
            self.hp = 500
            self.maxHp = 500
            self.atk = 60
            self.spd = 10
            self.defn = 80
        elif self.ourClass == 'Voidwalker':
            self.hp = 410
            self.maxHp = 410
            self.atk = 100
            self.spd = 30
            self.defn = 60
        elif self.ourClass == 'Warlock':
            self.hp = 350
            self.maxHp = 350
            self.atk = 140
            self.spd = 40
            self.defn = 40

    def printInfo(self):
        marqueeprint('[PLAYER DATA]')
        centerprint(lr_justify('Class:', str(self.ourClass), self.dataWidth))
        centerprint(lr_justify('Name:', str(self.name), self.dataWidth))
        centerprint(lr_justify('HP:', str(self.hp) + '/' + str(self.maxHp), self.dataWidth))
        centerprint(lr_justify('Gold:', str(self.gold), self.dataWidth))
        centerprint(lr_justify('Atk:', str(self.atk), self.dataWidth))
        centerprint(lr_justify('Defense:', str(self.defn), self.dataWidth))
        print('')

    def datadict(self):
        return {
            'Class': str(self.ourClass),
            'Name': str(self.name),
            'HP': str(str(self.hp) + '/' + str(self.maxHp)),
            'Gold': str(self.gold),
            'Atk': str(self.atk),
            'Def': str(self.defn)
        }
