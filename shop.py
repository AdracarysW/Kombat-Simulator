

class Shop():

    def __init__(self):

        print("What is your name?")
        name = input(self.CYAN + "?> " + self.END)
        print("Welcome to the SHOP, {}!\n".format(name.title()))
        for player in self.players:
            if (player.getName() == name.title()):
                ind = self.players.index(player)
        print("You currently have {} gold".format(self.players[ind].getGold()))
        print("Buy one: ")
        print('''
        1. Health Potion
        2. Speed Potion
        3. Attack Potion
        4. Defense Potion
        ''')
        num = int(input(self.CYAN + "?> " + self.END))
        if(num == 1):
            print("How many healing potions do you want?")
            amt1 = int(input(self.CYAN + "?> " + self.END))
            self.players[i].subtractGold(150)
        else:
            pass


        self.players[num].subtractGold(500)
