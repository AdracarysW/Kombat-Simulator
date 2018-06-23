

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
  
    def buyPotions(self, player, money):
        heal = 150
        speed = 50
        attack = 100
        defense = 150
        gold = money
        print("Welcome to the SHOP!")
        while (gold != 50):
            print("Current Gold: {}\n".format(gold))
            print("Potions")
            print("1. Health Potion")
            print("2. Speed Potion")
            print("3. Attack Potion")
            print("4. Defense Potion")
            
            num = int(input(self.CYAN + "?> " + self.END))
            if (num == 1):
                print("Number of HEALTH POTIONS: ")
                val = int(input(self.CYAN + "?> " + self.END))
                gold -= val * heal
                self.newDict["Health Potion"] = val
            elif (num == 2):
                print("Number of SPEED POTIONS: ")
                val = int(input(self.CYAN + "?> " + self.END))
                gold -= val * speed
                self.newDict["Speed Potion"] = val
            elif (num == 3):
                print("Number of ATTACK POTIONS: ")
                val = int(input(self.CYAN + "?> " + self.END))
                gold -= val * attack
                self.newDict["Attack Potion"] = val  
            elif (num == 4):
                print("Number of DEFENSE POTIONS: ")
                val = int(input(self.CYAN + "?> " + self.END))
                gold -= val * defense
                self.newDict["Defense Potion"] = val  
            else: 
                print(self.RED + "Invalid Entry" + self.END)
        return self.newDict
