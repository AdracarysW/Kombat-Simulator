
class Player():

    def __init__(self, name, health, speed, attack, defense):
        self.name = name
        self.hp = health
        self.spd = speed
        self.atk = attack
        self.dfn = defense
        self.gold = 1000
        self.inv = {"Health Potion" : 0, "Speed Potion" : 0, "Attack Potion" : 0, "Defense Potion" : 0}

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

    def getInvValues(self, key):
        return self.inv.get(key)

    def changeInvValues(self, key):
        self.inv[key] -= 1

    def changeInv(self, newDict):
        for key, value in newDict.items():
            self.inv[key] = value

    def decreaseGold(self, amount):
        self.gold -= amount

    def skill(self, character):
        if(character == "Arcstrider"):
            return "20% Chance for Arcstrider to halve its' opponent's life points!"
        elif(character == "Dawnblade"):
            return "20% Chance for recoil damage of 30 life points to Dawnblade!"
        elif(character == "Gunslinger"):
            return "50% Chance for Gunslinger to attack its' opponent twice!"
        elif (character == "Sentinel"):
            return "100% Chance for Sentinel to go through opponent's defense next turn!"
        elif (character == "Voidwalker"):
            return "30% Chance to dodge opponent's attack!"
        else:
            return "20% Chance to inflict lifesteal!"

    def increaseHealth(self):
        self.hp += 40
    
    def increaseSpeed(self):
        self.spd += 25

    def increaseAttack(self):
        self.atk += 30
    
    def increaseDefense(self):
        self.dfn += 40

    def attack(self):
        print(self.name + " attacks the enemy!")
        return self.atk

    def takeDamage(self, attack):
        self.hp -= attack - self.dfn
        damage = attack - self.dfn
        print(self.name + " took " + str(damage) + " amount of damage. Current health : " + str(self.hp))
        return attack - self.dfn
