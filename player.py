# this creates a class for the player
import datetime

class Player_stats:
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
        self.missions = []
        self.location = None
        self.traveling = False
        self.health = 100
        self.energy = 100
        self.race = None
        self.crew = []
        self.affiliations = []
        
    def greet(self):
        print(f"Hello, {self.name}!")
        print(f"Your ID is {self.id}.")
        print(f"You have {self.money} credits.")
        print(f"You have {self.health} health.")
