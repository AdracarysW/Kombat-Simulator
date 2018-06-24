from player import Player
from shop import Shop
from textTools import *

class Game():




    def gameloop(self):
        while True:
            marqueeprint('')
            centerprint('MiniRPG')
            centerprint('Colin Burke 2017')
            marqueeprint('')
            centerprint('[p]reparation [f]ight')
            decision = input()
            if decision == 'p' or decision == '':
                # Make new global hero and enemy which will change over time
                self.ourhero = self.newhero()
                self.ourenemy = self.getenemy()
                self.ourhero.heroperks()
                gridoutput(self.ourhero.datadict())
            if decision == 'l':
                print('lOADING GAME')
                self.ourhero = self.loadgame()
                self.ourenemy = self.getenemy()
            while self.ourhero.isalive():
                self.fight()