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
oneShop = False
twoShop = False
bool1 = False
bool2 = False

def addCharacters():
    global characters
    arc = Arcstrider()
    dawn = Dawnblade()
    gun = Gunslinger()
    sent = Sentinel()
    void = Voidwalker()
    war = Warlock()
    characters = [arc, dawn, gun, sent, void, war]

def canAddPlayers():
    global bool1
    global bool2
    print("Player One, are you ready? (Y/N)")
    ans1 = input(entry)
    if (ans1.upper() == "Y"):
        bool1 = True
        print("Player One ready!")
    elif ((ans1.upper() != "Y") or (ans1.upper() != "N")):
        mainMenuError("Invalid Selection")
    print("Player Two, are you ready? (Y/N)")
    ans2 = input(entry)
    if (ans2.upper() == "Y"):
        bool2 = True
        print("Player Two ready!")
    elif ((ans2.upper() != "Y") and (ans2.upper() != "N")):
        mainMenuError("Invalid Selection")
    if ((bool1) and (bool2)):
        return True
    else:
        return False

def addPlayers():
    selectionOne()
    selectionTwo()

def addPlayerOne(character):
    global playerOne
    global characters
    for person in characters:
        if (person.getName() == character):
            playerOne.append(person)

def addPlayerTwo(character):
    global playerTwo
    global characters
    for person in characters:
        if (person.getName() == character):
            playerTwo.append(person)

def selectionOne():
    global select1
    global names
    showCharacters() #shows all characters
    while(True):
        print("Player 1: Choose your character")
        select1 = input(entry)
        for name in names:
            if (select1 == name):
                addPlayerOne(select1.title())
                return
        print("Invalid selection")

def showCharacters():
    global characters
    for person in characters:
        print("")
        print("{}".format(BOLD + person.getName() + END))
        print("Health:  {}".format(person.getHealth()))
        print("Speed:   {}".format(person.getSpeed()))
        print("Attack:  {}".format(person.getAttack()))
        print("Defense: {}\n".format(person.getDefense()))


def selectionTwo():
    global select1
    global select2
    global names
    showCharacters()
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

def canLobby(bool):
    return bool

def lobby():
    viewPlayerOne()
    viewPlayerTwo()

def viewPlayerOne(): #shows the stats of player one
    global playerOne
    global BOLD
    global END
    print("Player 1")
    print("")
    print(BOLD + playerOne[0].getName() + END)
    print("Health:  {}".format(playerOne[0].getHealth()))
    print("Speed:   {}".format(playerOne[0].getSpeed()))
    print("Attack:  {}".format(playerOne[0].getAttack()))
    print("Defense: {}\n".format(playerOne[0].getDefense()))
    print("Gold: {}\n".format(playerOne[0].getGold()))
    print("Potions: ")
    print("  Health  -> {}".format(playerOne[0].getInvValues("Health Potion")))
    print("  Speed   -> {}".format(playerOne[0].getInvValues("Speed Potion")))
    print("  Attack  -> {}".format(playerOne[0].getInvValues("Attack Potion")))
    print("  Defense -> {}\n".format(playerOne[0].getInvValues("Defense Potion")))
    print("Wins: {}".format(playerOne[0].getWins()))
    print("Losses: {}".format(playerOne[0].getLosses()))

def viewPlayerTwo(): #shows the stats of player one
    global playerTwo
    global BOLD
    global END
    print("Player 2")
    print("")
    print("{}".format(BOLD + playerTwo[0].getName() + END))
    print("Health:  {}".format(playerTwo[0].getHealth()))
    print("Speed:   {}".format(playerTwo[0].getSpeed()))
    print("Attack:  {}".format(playerTwo[0].getAttack()))
    print("Defense: {}\n".format(playerTwo[0].getDefense()))
    print("Gold: {}\n".format(playerTwo[0].getGold()))
    print("Potions: ")
    print("  Health  -> {}".format(playerTwo[0].getInvValues("Health Potion")))
    print("  Speed   -> {}".format(playerTwo[0].getInvValues("Speed Potion")))
    print("  Attack  -> {}".format(playerTwo[0].getInvValues("Attack Potion")))
    print("  Defense -> {}\n".format(playerTwo[0].getInvValues("Defense Potion")))
    print("Wins: {}".format(playerTwo[0].getWins()))
    print("Losses: {}".format(playerTwo[0].getLosses()))


def fight():
    global playerOne
    global playerTwo
    i = 3
    print("Battle will commence between {} and {}!".format(playerOne[0].getName(), playerTwo[0].getName()))
    while (i >= 0):
        print(str(i) + "...")
        time.sleep(1)
        i -= 1
    while((playerOne[0].getHealth() > 0) and (playerTwo[0].getHealth())):
        fightTurnOne()
        fightTurnTwo()
    if (playerOne[0].getHealth() <= 0):
        print("Player Two wins the fight!")
    else:
        print("Player One wins the fight!")


def canBattle():
    global bool1
    global bool2
    if (bool1 and bool2):
        return True
    else: 
        return False


def fightTurnOne():
    global entry
    global playerOne
    global playerTwo
    print('''
    Fight Menu:
    1. Attack
    2. Potion
    3. Skill
    ''')
    move = int(input(entry))
    if (move == 1):
        playerTwo[0].takeDamage(playerOne[0].getAttack())
        print("Player One attacks Player Two. \n P2 HP: {}".format(playerTwo[0].getHealth()))
    elif (move == 2):
        print("Potions:")
        if (playerOne[0].getInvValues("Health Potion") > 0):
            print("1. Health Potion")
        elif (playerOne[0].getInvValues("Speed Potion") > 0):
            print("2. Speed Potion")
        elif (playerOne[0].getInvValues("Attack Potion") > 0):
            print("3. Attack Potion")
        elif (playerOne[0].getInvValues("Defense Potion") > 0):
            print("4. Defense Potion")
        else:
            print("You don't have any potions")
        choice = int(input(entry))   
        if (choice == 1):
            playerOne[0].increaseHealth()
            playerOne[0].changeInvValues("Health Potion")
        elif (choice == 2):
            playerOne[0].increaseSpeed()
            playerOne[0].changeInvValues("Speed Potion")
        elif (choice == 3):
            playerOne[0].increaseAttack()
            playerOne[0].changeInvValues("Attack Potion")
        elif (choice == 4):
            playerOne[0].increaseDefense()
            playerOne[0].changeInvValues("Defense Potion")
        else:
            print("Not one of the choices")
    elif (move == 3):
        playerOne[0].skill(playerOne[0].getName())
    else:
        mainMenuError("You've done goofed")
        

def fightTurnTwo():
    global entry
    global playerOne
    global playerTwo
    print('''
    Fight Menu:
    1. Attack
    2. Potion
    3. Skill
    ''')
    move = int(input(entry))
    if (move == 1):
        playerOne[0].takeDamage(playerTwo[0].getAttack())
        print("Player One attacks Player Two. \n P2 HP: {}".format(playerTwo[0].getHealth()))
    elif (move == 2):
        print("Potions:")
        if (playerTwo[0].getInvValues("Health Potion") > 0):
            print("1. Health Potion")
        elif (playerTwo[0].getInvValues("Speed Potion") > 0):
            print("2. Speed Potion")
        elif (playerTwo[0].getInvValues("Attack Potion") > 0):
            print("3. Attack Potion")
        elif (playerTwo[0].getInvValues("Defense Potion") > 0):
            print("4. Defense Potion")
        else:
            print("You don't have any potions")
        choice = int(input(entry))   
        if (choice == 1):
            playerTwo[0].increaseHealth()
            playerTwo[0].changeInvValues("Health Potion")
        elif (choice == 2):
            playerTwo[0].increaseSpeed()
            playerTwo[0].changeInvValues("Speed Potion")
        elif (choice == 3):
            playerTwo[0].increaseAttack()
            playerTwo[0].changeInvValues("Attack Potion")
        elif (choice == 4):
            playerTwo[0].increaseDefense()
            playerTwo[0].changeInvValues("Defense Potion")
        else:
            print("Not one of the choices")
    elif (move == 3):
        playerTwo[0].skill(playerOne[0].getName())
    else:
        mainMenuError("You've done goofed")

def mainMenu():
    screen = ""
    screen += ("Main Menu\n")
    screen += ("1. Players\n")
    screen += ("2. Lobby\n")
    screen += ("3. Battle\n")
    screen += ("4. Shop\n")
    screen += ("5. Quit\n")
    return screen

def mainMenuError(err):
    global BOLD
    global RED
    global END
    err.upper()
    print(BOLD + RED + err + END)

def main():
    addCharacters()
    while(True):
        print(mainMenu())
        location = int(input(entry)) # maybe str
        while location not in [1, 2, 3, 4, 5]:
            print(mainMenu())
            location = int(input(entry))
        if (location == 1): #Players
            if (canAddPlayers()):
                addPlayers()
                canLobby(True)
            else:
                mainMenuError("Two players required to play!")
        elif (location == 2): #Lobby
            if (canLobby(True)):
                lobby()
            else:
                pass
        elif (location == 3): #Battle
            if (canBattle()):
                fight()
            else:
                mainMenuError("You need two PLAYERS in order to fight!")
        elif (location == 4): #Shop
            if (canShop()):
                goShopping()
            else:
                mainMenuError("Neither players have sufficient gold to buy anything.")
        elif (location == 5): #Quit
            if (canQuit()):
                return
            else:
                print("Exiting...")
        else:
            mainMenuError("You've done goofed.")

def canQuit():
    global entry
    print("Are you sure you want to quit? (Y/N)")
    var = input(entry)
    if(var.upper() == "Y"):
        return True
    else:
        return False


def canShop():
    global oneShop
    global twoShop
    if (canShopOne() or canShopTwo()):
        return True
    else:
        return False

def canShopOne():
    global oneShop
    print("Player One")
    print("Current inventory ")
    print("Gold: {}\n".format(playerOne[0].getGold()))
    print("Potions: ")
    print("  Health  -> {}".format(playerOne[0].getInvValues("Health Potion")))
    print("  Speed   -> {}".format(playerOne[0].getInvValues("Speed Potion")))
    print("  Attack  -> {}".format(playerOne[0].getInvValues("Attack Potion")))
    print("  Defense -> {}\n".format(playerOne[0].getInvValues("Defense Potion")))
    if (playerOne[0].getGold() >= 50):
        print("You have sufficient gold, you may proceed.")
        oneShop = True
        return True
    else: 
        ("Player One has insufficient gold, you cannot buy anything.")
        return False

def canShopTwo():
    global twoShop
    print("Player Two")
    print("Current inventory ")
    print("Gold: {}\n".format(playerTwo[0].getGold()))
    print("Potions: ")
    print("  Health  -> {}".format(playerTwo[0].getInvValues("Health Potion")))
    print("  Speed   -> {}".format(playerTwo[0].getIntValues("Speed Potion")))
    print("  Attack  -> {}".format(playerTwo[0].getIntValues("Attack Potion")))
    print("  Defense -> {}\n".format(playerTwo[0].getIntValues("Defense Potion")))
    if (playerTwo[0].getGold() >= 50):
        print("You have sufficient gold, you may proceed.")
        twoShop = True
        return True
    else: 
        ("Player Two has insufficient gold, you cannot buy anything.")
        return False

def goShopping():
    global oneShop, twoShop
    sh = Shop()
    if (oneShop and twoShop):
        playerOne[0].changeInv(sh.buyPotions(playerOne[0], playerOne[0].getGold()))
        playerTwo[0].changeInv(sh.buyPotions(playerTwo[0], playerTwo[0].getGold()))
    elif (oneShop):
        playerOne[0].changeInv(sh.buyPotions(playerOne[0], playerOne[0].getGold()))
    else:
        playerTwo[0].changeInv(sh.buyPotions(playerTwo[0], playerTwo[0].getGold()))

main()









    