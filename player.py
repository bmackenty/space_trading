# this creates a class for the player
import datetime

class player:
    def __init__(self,name):
        self.name = name
        self.id = None 
        self.money = 1000
        self.ship = None
        self.cargo = []
        self.weapons = []
        self.upgrades = []
        self.faction = None
        self.reputation = 0
        self.skills = {}
        self.stats = {"strength":0,"dexterity":0,"constitution":0,"intelligence":0,"wisdom":0,"charisma":0,"luck":0,"ether":0}
        self.missions = []
        self.location = None
        self.traveling = False
        self.health = 100
        self.energy = 100
        self.race = None
        self.crew = []
        self.affiliations = []
        self.race = None
        self._createDate = datetime.datetime.now()
                
    def greet(self):
        # print(f"Hello, {self.name}!")
        # print(f"Your ID is {self.id}.")
        # print(f"You have {self.money} credits.")
        # print(f"You have {self.health} health.")
        # print(f"Stats: {self.stats}")
        # print(f"Create Date: {self._createDate}")
        return f"Hello, {self.name}! \nYour ID is {self.id}.\n You have {self.money} credits. You have {self.health} health."
    
    # function for users setup (or create) their player
    def setup(self):
        self.name = input("What is your name? ")

     
