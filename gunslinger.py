from player import Player
import random

class Gunslinger(Player):

    def __init__(self, name):
        super().__init__("Gunslinger", name, 330, 50, 80, 40)

    def skill(self):
        if (random.randint(0, 100) < 50):
            if(players.getHer):
                players[villian].takeDamage(players[hero].getAttack())
            else:
                players[hero].takeDamage(players[villian].getAttack())
        else:
            pass
