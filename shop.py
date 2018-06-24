

class Shop():

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
        self.newDict = {"Health Potion" : 0, "Speed Potion" : 0, "Attack Potion" : 0, "Defense Potion" : 0}
        self.gold = 0
        self.heal = 150
        self.speed = 50
        self.attack = 100
        self.defense = 150

    def buyPotions(self, player, gold):
        self.gold += gold
        print("Welcome to the SHOP!")
        while (self.gold != 0):
            print("Current Gold: {}\n".format(self.gold))
            print("Potions")
            print("1. Health Potion")
            print("2. Speed Potion")
            print("3. Attack Potion")
            print("4. Defense Potion")
            num = int(input(self.CYAN + "?> " + self.END))
            if (self.calculate(num)):
                continue
        return self.newDict
    
    def amtGold(self):
        return self.gold

    def calculate(self, num):
        if (num == 1):
            print("Number of HEALTH POTIONS: ")
            val = int(input(self.CYAN + "?> " + self.END))
            if (self.gold >= val * self.heal):
                self.gold -= val * self.heal
                self.newDict["Health Potion"] += val
                return True
        elif (num == 2):
            print("Number of SPEED POTIONS: ")
            val = int(input(self.CYAN + "?> " + self.END))
            if (self.gold >= val * self.speed):                   
                self.gold -= val * self.speed
                self.newDict["Speed Potion"] += val
                return True
            else:
                print(self.RED + self.BOLD + "Insufficient Gold" + self.END)
        elif (num == 3):
            print("Number of ATTACK POTIONS: ")
            val = int(input(self.CYAN + "?> " + self.END))
            if (self.gold >= val * self.attack):                   
                self.gold -= val * self.attack
                self.newDict["Attack Potion"] += val  
                return True
            else: 
                print(self.RED + self.BOLD + "Insufficient Gold" + self.END)
        elif (num == 4):
            print("Number of DEFENSE POTIONS: ")
            val = int(input(self.CYAN + "?> " + self.END))
            if (self.gold >= val * self.defense):
                self.gold -= val * self.defense
                self.newDict["Defense Potion"] += val  
                return True
            else:
                print(self.RED + self.BOLD + "Insufficient Gold" + self.END)
        else: 
            print(self.RED + "Invalid Entry" + self.END)
