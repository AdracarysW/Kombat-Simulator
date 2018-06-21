
class Player():

    def __init__(self, name, health, speed, attack, defense):
        self.name = name
        self.hp = health
        self.spd = speed
        self.atk = attack
        self.dfn = defense
        self.gold = 1000
        self.inv = {}
        self.win = 0
        self.loss = 0

    def getJob(self):
        return self.job

    def getName(self):
        return self.name

    def getHealth(self):
        return self.hp

    def getSpeed(self):
        return self.spd

    def getAttack(self):
        return self.atk

    def getDefense(self):
        return self.dfn

    def getGold(self):
        return self.gold

    def attack(self):
        print(self.name + " attacks the enemy!")
        return self.atk

    def takeDamage(self, attack):
        self.hp -= attack - self.dfn
        damage = attack - self.dfn
        print(self.name + " took " + str(damage) + " amount of damage. Current health : " + str(self.hp))
        return attack - self.dfn
