
from game import Game
from textTools import *

class Player():

    def __init__(self, playerClass, name):
        self.ourClass = playerClass
        self.name = ''
        self.hp = 0
        self.atk = 0
        self.spd = 0
        self.defn = 0
        self.mana = 0
        self.gold = 100
        self.isBattling = False
        self.dataWith = 40

    def canAfford(self, val):
        if self.gold >= val:
            return True
        else:
            return False

    def death(self):
        self.isBattling = False
        self.hp = 0

    def isAlive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def playerPerks(self):
        if self.ourClass == 'arcstrider':
            self.hp = 300
            self.atk = 90
            self.spd = 60
            self.defn = 50
        elif self.ourClass == 'dawnblade':
            self.hp = 450
            self.atk = 160
            self.spd = 20
            self.defn = 20
        elif self.ourClass == 'gunslinger':
            self.hp = 330
            self.atk = 80
            self.spd = 50
            self.defn = 40
        elif self.ourClass == 'sentinel':
            self.hp == 500
            self.atk = 60
            self.spd = 10
            self.defn = 80
        elif self.ourClass == 'voidwalker':
            self.hp == 410
            self.atk == 100
            self.spd = 30
            self.defn = 60
        elif self.ourClass == 'warlock':
            self.hp == 350
            self.atk == 140
            self.spd = 40
            self.defn = 40

    def printInfo(self):
       marqueeprint('[HERO DATA]')
        centerprint(Game.lr_justify('Class:', str(self.ourclass), self.datawidth))
        centerprint(Game.lr_justify('Name:', str(self.name), self.datawidth))
        centerprint(Game.lr_justify('Level:', str(self.level), self.datawidth))
        centerprint(Game.lr_justify('XP:', str(self.xp) + '/' + str(self.nextlevel), self.datawidth))
        centerprint(Game.lr_justify('HP:', str(self.hp) + '/' + str(self.maxhp), self.datawidth))
        centerprint(Game.lr_justify('Gold:', str(self.gold), self.datawidth))
        centerprint(Game.lr_justify('Atk:', str(self.atk), self.datawidth))
        centerprint(Game.lr_justify('Defense:', str(self.defn), self.datawidth))
        centerprint(Game.lr_justify('Dodge:', str(self.dodge), self.datawidth))
        centerprint(Game.lr_justify('battles fought', str(self.battlecount), self.datawidth))
        print('')
