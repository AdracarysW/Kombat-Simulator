from player import Player
from arcstrider import Arcstrider
from dawnblade import Dawnblade
from gunslinger import Gunslinger
from sentinel import Sentinel
from voidwalker import Voidwalker
from warlock import Warlock
import description
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

def addPlayerOne(self, character):
    global playerOne
    global characters
    for person in characters:
        if (person.getName() == character):
            playerOne.append(person)
        else:
            continue

def addPlayerTwo(self, character):
    global playerTwo
    global characters
    for person in characters:
        if (person.getName() == character):
            playerTwo.append(person)

def selectionOne(self):
    global select1
    global names
    lobby()
    while(True)
        print("Player 1: Choose your character")
        select1 = input(entry)
        for name in names:
            if select1 == name:
                addPlayerOne(select1.title())
                return
        print("Invalid selection")
     
    
def selectionTwo(self):
    global select1
    global select2
    lobby()
    print("Player 2: Choose a different character")
    select2 = input(entry)
    if (select2 == select1):
        print("ERROR\n" + "Choose a different character")
    else: 
        addPlayerTwo(select2.title())




def lobby(self):
    i = 0
    if(len(players) == 0):
        print("Lobby is empty\n" + "No PLAYERS have joined\n")
    else:
        print("")
        while(i < len(players)):
            print(players[i].getJob() + ": " + players[i].getName())
            print("Health: " + str(players[i].getHealth()))
            print("Speed: " + str(players[i].getSpeed()))
            print("Attack: " + str(players[i].getAttack()))
            print("Defense: " + str(players[i].getDefense()))
            print("")
            i += 1

def battle(self):


def fightTurn(self):


def menu(self):
    global entry
    print('''
    Main Menu:
    1. Characters
    2. Lobby
    3. Battle
    4. Shop
    5. Quit
    ''')
    num = int(input(entry))

    if num == 1:
        self.description()
    elif num == 2:
        self.createPlayer()
    elif num == 3:
        self.lobby()
    elif num == 4:
        self.playArena()
    elif num == 5:
        self.shop()
    elif num == 6:
        self.quit()
    else:
        print("Please provide a number")
        menu()
    
def main(self):

