# this creates a class for the player

class Player_stats:
    def __init__(self):
        self.name = "none"
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

    def create_player(self):
        self.name = input("What is your name? ")
        print("Welcome, " + self.name + ".")
        print("You have 1000 credits to start with.")
        self.money = 1000

