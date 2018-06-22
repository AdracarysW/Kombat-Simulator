from player import Player
from arcstrider import Arcstrider
from dawnblade import Dawnblade
from gunslinger import Gunslinger
from sentinel import Sentinel
from voidwalker import Voidwalker
from warlock import Warlock
from description import description
from shop import Shop
import time

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

characters = []
playerOne = []
playerTwo = []
names = ["Arcstrider", "Dawnblade", "Gunslinger", "Sentinel", "Voidwalker", "Warlock"]
select1 = ""
select2 = ""
entry = CYAN + "?> " + END

def addCharacters(self):
    global characters
    arc = Arcstrider()
    dawn = Dawnblade()
    gun = Gunslinger()
    sent = Sentinel()
    void = Voidwalker()
    war = Warlock()
    characters.append(arc)
    characters.append(dawn)
    characters.append(gun)
    characters.append(sent)
    characters.append(void)
    characters.append(war)

def canAddPlayers(self):
    bool1 = False
    bool2 = False
    print("Player One, are you ready? (Y/N)")
    ans1 = input(entry)
    if (ans1.upper() == "Y"):
        bool1 = True
        print("Player One ready!")

        addPlayerOne(put)
    elif ((ans1.upper() != "Y") or (ans1.upper() != "N")):
        mainMenuError("Invalid Selection")
    print("Player Two, are you ready? (Y/N)")
    ans2 = input(entry)
    if (ans2.upper() == "Y"):
        bool2 = True
    elif ((ans2.upper() != "Y") or (ans2.upper() != "N")):
        mainMenuError("Invalid Selection")
    if ((bool1) and (bool2)):
        return True
    else:
        return False


def addPlayerOne(self, character):
    global playerOne
    global characters
    for person in characters:
        if (person.getName() == character):
            playerOne.append(person)

def addPlayerTwo(self, character):
    global playerTwo
    global characters
    for person in characters:
        if (person.getName() == character):
            playerTwo.append(person)

def selectionOne(self):
    global select1
    global names
    lobby() #shows all characters
    while(True):
        print("Player 1: Choose your character")
        select1 = input(entry)
        for name in names:
            if (select1 == name):
                addPlayerOne(select1.title())
                return
        print("Invalid selection")

def lobby(self):
    global characters
    for person in characters:
        print("")
        print("{}".format(BOLD + person.getName() + END))
        print("Health:  {}".format(person.getHealth()))
        print("Speed:   {}".format(person.getSpeed()))
        print("Attack:  {}".format(person.getAttack()))
        print("Defense: {}\n".format(person.getDefense()))


def selectionTwo(self):
    global select1
    global select2
    global names
    lobby()
    while(True):
        print("Player 2: Choose a different character")
        select2 = input(entry)
        if (select2 == select1):
            print("ERROR\n" + "Choose a different character")
        else:
            for name in names:
                if (select2 == name):
                    addPlayerTwo(select2.title())
                    return
            print("Invalid selection")

def viewPlayerOne(self): #shows the stats of player one
    global playerOne
    global BOLD
    global END
    print("Player 1")
    print("")
    print("{}".format(BOLD + playerOne.getName() + END))
    print("Health:  {}".format(playerOne.getHealth()))
    print("Speed:   {}".format(playerOne.getSpeed()))
    print("Attack:  {}".format(playerOne.getAttack()))
    print("Defense: {}\n".format(playerOne.getDefense()))
    print("Gold: {}\n".format(playerOne.getGold()))
    print("Potions: ")
    print("  Health  -> {}".format(playerOne.getInvValues("Health Potion")))
    print("  Speed   -> {}".format(playerOne.getIntValues("Speed Potion")))
    print("  Attack  -> {}".format(playerOne.getIntValues("Attack Potion")))
    print("  Defense -> {}\n".format(playerOne.getIntValues("Defense Potion")))
    print("Wins: {}".format(playerOne.getWins()))
    print("Losses: {}".format(playerOne.getLosses()))

def viewPlayerTwo(self): #shows the stats of player one
    global playerTwo
    global BOLD
    global END
    print("Player 2")
    print("")
    print("{}".format(BOLD + playerTwo.getName() + END))
    print("Health:  {}".format(playerTwo.getHealth()))
    print("Speed:   {}".format(playerTwo.getSpeed()))
    print("Attack:  {}".format(playerTwo.getAttack()))
    print("Defense: {}\n".format(playerTwo.getDefense()))
    print("Gold: {}\n".format(playerTwo.getGold()))
    print("Potions: ")
    print("  Health  -> {}".format(playerTwo.getInvValues("Health Potion")))
    print("  Speed   -> {}".format(playerTwo.getIntValues("Speed Potion")))
    print("  Attack  -> {}".format(playerTwo.getIntValues("Attack Potion")))
    print("  Defense -> {}\n".format(playerTwo.getIntValues("Defense Potion")))
    print("Wins: {}".format(playerTwo.getWins()))
    print("Losses: {}".format(playerTwo.getLosses()))


def battle(self):
    pass

def fightTurn(self):
    pass

def menu(self):
    screen += ("Main Menu")
    screen += ("1. Players")
    screen += ("2. Lobby")
    screen += ("3. Battle")
    screen += ("4. Shop")
    screen += ("5. Quit\n")
    return screen

def mainMenuError(self, err):
    global BOLD
    global RED
    global END
    err.upper()
    print(BOLD + RED + err + END)

def main(self):
    addCharacters()
    while(True):
        print(mainMenu())
        location = int(input(entry)) # maybe str
        while location not in [1, 2, 3, 4, 5]:
            print(mainMenu("Invalid Selection"))
            location = int(input(entry))
        if (location == 1): #Players
            if (canAddPlayers()):
                addPlayers()
                    addPlayerOne()
                    addPlayerTwo()
            else:
                mainMenuError("Two players required to play!")
        elif (location == 2): #Lobby
            if (canLobby()):
                pass
            else:
                pass
        elif (location == 3): #Battle
            if (canBattle()):
                Fight()
            else:
                pass
        elif (location == 4): #Shop
            if (canShop()):
                goShopping()
                    Shop.method(player[0])
            else:
                pass
        elif (location == 5): #Quit
            if (canQuit())):
                pass
            else:
                pass
        else:
            mainMenuError("You've done goofed.")
